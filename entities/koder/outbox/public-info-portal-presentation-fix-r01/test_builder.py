#!/usr/bin/env python3
import json, tempfile, unittest
from pathlib import Path
from types import ModuleType
import sys
_builder_path=Path(__file__).resolve().parent/"builder.py"
builder=ModuleType("_portal_builder_subject");builder.__file__=str(_builder_path);sys.modules[builder.__name__]=builder
exec(compile(_builder_path.read_bytes(),str(_builder_path),"exec"),builder.__dict__)
class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=Path(__file__).resolve().parent/"inputs"
    def test_reproducible(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            ma=builder.build(self.inputs,Path(a));mb=builder.build(self.inputs,Path(b))
            self.assertEqual(builder.tree_digest(Path(a)),builder.tree_digest(Path(b)))
            self.assertEqual(ma,mb)
    def test_routes_and_static_only(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);m=builder.build(self.inputs,out)
            routes=json.loads((out/"routes.json").read_text())["routes"]
            rm=json.loads((self.inputs/"route-map.json").read_text())
            led=json.loads((self.inputs/"content-eligibility-ledger.json").read_text())
            expected={x["route"] for x in rm["routes"]}|{x["portal_route"] for x in led["entries"]}
            self.assertEqual({x["route"] for x in routes},expected)
            self.assertEqual(m["routes_count"],len(expected))
            self.assertTrue(all(p.suffix in (".html",".css",".json") for p in out.rglob("*") if p.is_file()))
            self.assertFalse(any(p.suffix in (".db",".sqlite",".sqlite3") for p in out.rglob("*") if p.is_file()))
    def test_banner_and_empty_states(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            for p in out.rglob("*.html"): self.assertIn(builder.BANNER,p.read_text())
            self.assertIn("Публичное представление кооперации ещё не прошло необходимую проверку", (out/"cooperation/index.html").read_text())
            self.assertIn("Для этой версии ещё не выбран утверждённый публичный индекс публикаций", (out/"publications/index.html").read_text())
            self.assertIn("В эту версию не включены проверенные публично допустимые объекты", (out/"withdrawn/index.html").read_text())
    def test_presentation_titles(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            self.assertIn("Ожидающие проверки и ограничения",(out/"status/gates/index.html").read_text())
            self.assertIn("История и заменённые версии",(out/"history/index.html").read_text())
    def test_candidate_stale_labels(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            self.assertIn("Черновик",(out/"project/what-is-wellbeing/index.html").read_text())
            self.assertIn("Актуальность не подтверждена",(out/"status/log16/index.html").read_text())
    def test_hq_metadata_only(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            txt=(out/"developments/entity-ai-resource-boosters/index.html").read_text()
            self.assertIn("Направление разработки, проходящее отдельные технические проверки",txt)
            self.assertNotIn("Current gate:",txt)
    def test_fail_closed_input_identity(self):
        with tempfile.TemporaryDirectory() as x, tempfile.TemporaryDirectory() as d:
            dst=Path(x)
            import shutil;shutil.copytree(self.inputs,dst,dirs_exist_ok=True)
            p=dst/"route-map.json";p.write_bytes(p.read_bytes()+b"\n")
            with self.assertRaisesRegex(builder.BuildError,"SOURCE_IDENTITY_MISMATCH"):
                builder.build(dst,Path(d))
    def test_manifest_readback(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            m=json.loads((out/"build-manifest.json").read_text())
            for rel,meta in m["files"].items():
                data=(out/rel).read_bytes()
                self.assertEqual(builder.sha256(data),meta["sha256"]);self.assertEqual(len(data),meta["bytes"])
    def test_no_public_ready_promotion(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            self.assertFalse(json.loads((out/"build-manifest.json").read_text())["public_ready"])
            self.assertFalse(json.loads((out/"routes.json").read_text())["public_ready"])
    def test_all_primary_titles_are_russian_human_labels(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            routes=json.loads((out/"routes.json").read_text())["routes"]
            ledger=json.loads((self.inputs/"content-eligibility-ledger.json").read_text())
            ids={e["id"] for e in ledger["entries"]}
            for r in routes:
                text=(out/r["file"]).read_text()
                import re
                title=re.search(r"<title>(.*?)</title>",text).group(1)
                h1=re.search(r"<h1>(.*?)</h1>",text).group(1)
                self.assertEqual(title,h1)
                self.assertRegex(title,r"[А-Яа-яЁё]")
                for internal_id in ids:
                    self.assertNotIn(internal_id.replace("-"," "),title)
                    self.assertNotIn(internal_id,title)

    def test_every_candidate_has_visible_candidate_badge(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            ledger=json.loads((self.inputs/"content-eligibility-ledger.json").read_text())
            candidates=[e for e in ledger["entries"] if e["semantic_bucket"]=="candidate" or e["representation_state"]=="preview_candidate"]
            self.assertGreater(len(candidates),0)
            for e in candidates:
                target=builder.route_file(out,e["portal_route"])
                self.assertIn('<span class="badge">Кандидат</span>',target.read_text())

    def test_internal_id_only_in_secondary_provenance(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);builder.build(self.inputs,out)
            ledger=json.loads((self.inputs/"content-eligibility-ledger.json").read_text())
            for e in ledger["entries"]:
                text=builder.route_file(out,e["portal_route"]).read_text()
                self.assertIn("Технические сведения и происхождение",text)
                self.assertIn(e["id"],text)
                before=text.split("Технические сведения и происхождение",1)[0]
                self.assertNotIn(e["id"],before)

if __name__=="__main__":
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print(json.dumps({"verdict":"PASS_PORTAL_STATIC_BUILD_TESTS","tests":r.testsRun,"failures":len(r.failures),"errors":len(r.errors),"skipped":len(r.skipped)},sort_keys=True))
    raise SystemExit(0 if r.wasSuccessful() else 1)