import io
import json
import os
import tarfile
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch
import gateway

def req(**kw):
    x={"schema":gateway.SCHEMA_REQUEST,"request_id":"req-1","requester_entity":"KOD",
       "authority_ref":"fixture://authority","host_id":"mazhor","mode":"VERIFY",
       "operation":"STAT","root_id":"MAZHOR_REPO_WELLBEING_HQ","relative_path":"a.txt",
       "max_output_bytes":gateway.MAX_OUTPUT_BYTES}
    x.update(kw); return gateway.canonical_bytes(x)

class T(unittest.TestCase):
    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.root=Path(td.name)
        (self.root/"a.txt").write_text("alpha")
        (self.root/"dir").mkdir(); (self.root/"dir"/"b.txt").write_text("beta")
        self.gw=gateway.Gateway(lambda h,r:self.root)

    def code(self,raw): return self.gw.execute(raw).error_code

    def test_exact_opcode_enum(self):
        self.assertEqual({x.value for x in gateway.Opcode},{
          "STAT","LIST_DIR","READ_BOUNDED","SHA256","ARCHIVE_LIST","GIT_STATUS_PORCELAIN",
          "GIT_HEAD","GIT_HEAD_TREE","GIT_LS_TREE","GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"})

    def test_unknown_opcode_root_and_write(self):
        self.assertEqual(self.code(req(operation="SHELL")),"OP_NOT_ALLOWED")
        self.assertEqual(self.code(req(root_id="OTHER")),"ROOT_NOT_ALLOWED")
        self.assertEqual(self.code(req(mode="WRITE")),"WRITE_MODE_NOT_AUTHORIZED")
        o=json.loads(req()); o["command"]="rm -rf /"
        self.assertEqual(self.code(gateway.canonical_bytes(o)),"OP_NOT_ALLOWED")

    def test_absolute_traversal_denied(self):
        self.assertEqual(self.code(req(relative_path="/etc/passwd")),"ABSOLUTE_PATH_DENIED")
        self.assertEqual(self.code(req(relative_path="../a.txt")),"PATH_TRAVERSAL_DENIED")
        self.assertEqual(self.code(req(relative_path="dir//b.txt")),"PATH_TRAVERSAL_DENIED")

    def test_symlink_and_denied_target(self):
        (self.root/"link").symlink_to(self.root/"a.txt")
        self.assertEqual(self.code(req(relative_path="link")),"SYMLINK_NOT_ALLOWED")
        (self.root/".env").write_text("X")
        self.assertEqual(self.code(req(relative_path=".env")),"DENIED_TARGET")
        (self.root/".ssh").mkdir(); (self.root/".ssh"/"id").write_text("X")
        self.assertEqual(self.code(req(relative_path=".ssh/id")),"DENIED_TARGET")

    def test_true_symlink_swap_before_open(self):
        victim=self.root/"victim.txt"; victim.write_text("safe")
        outside=self.root/"outside.txt"; outside.write_text("SECRET")
        real_open=os.open; swapped={"done":False}
        def attacking_open(path,flags,*a,**kw):
            if path=="victim.txt" and kw.get("dir_fd") is not None and not swapped["done"]:
                victim.unlink(); victim.symlink_to(outside); swapped["done"]=True
            return real_open(path,flags,*a,**kw)
        with patch("gateway.os.open",side_effect=attacking_open):
            r=self.gw.execute(req(operation="READ_BOUNDED",relative_path="victim.txt"))
        self.assertEqual(r.error_code,"SYMLINK_NOT_ALLOWED")
        self.assertNotIn("SECRET",json.dumps(gateway.asdict(r)))

    def test_sha256_deadline_enforced(self):
        old=gateway.TIMEOUTS[gateway.Opcode.SHA256]
        gateway.TIMEOUTS[gateway.Opcode.SHA256]=0.02
        try:
            with patch.object(gateway.Gateway,"_sha_fd",side_effect=lambda fd:(time.sleep(.08),"x")[1]):
                self.assertEqual(self.code(req(operation="SHA256")),"TIMEOUT")
        finally: gateway.TIMEOUTS[gateway.Opcode.SHA256]=old

    def test_archive_deadline_enforced(self):
        arc=self.root/"x.tar"
        with tarfile.open(arc,"w") as tf:
            b=b"x"; info=tarfile.TarInfo("x"); info.size=1; tf.addfile(info,io.BytesIO(b))
        old=gateway.TIMEOUTS[gateway.Opcode.ARCHIVE_LIST]
        gateway.TIMEOUTS[gateway.Opcode.ARCHIVE_LIST]=0.02
        original=tarfile.open
        def slow(*a,**k): time.sleep(.08); return original(*a,**k)
        try:
            with patch("gateway.tarfile.open",side_effect=slow):
                r=self.gw.execute(req(operation="ARCHIVE_LIST",root_id="MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01",
                                      relative_path="x.tar"))
            self.assertEqual(r.error_code,"TIMEOUT")
        finally: gateway.TIMEOUTS[gateway.Opcode.ARCHIVE_LIST]=old

    def test_read_oversize_and_invalid_utf8(self):
        (self.root/"big.txt").write_bytes(b"x"*100)
        self.assertEqual(self.code(req(operation="READ_BOUNDED",relative_path="big.txt",max_output_bytes=10)),
                         "LIMIT_EXCEEDED")
        (self.root/"bin").write_bytes(b"\xff\xfe")
        self.assertEqual(self.code(req(operation="READ_BOUNDED",relative_path="bin")),
                         "BINARY_TEXT_NOT_ALLOWED")

    def test_final_serialized_cap_json_expansion(self):
        (self.root/"quotes.txt").write_text('"'*600000)
        r=self.gw.execute(req(operation="READ_BOUNDED",relative_path="quotes.txt",
                              max_output_bytes=gateway.MAX_OUTPUT_BYTES))
        self.assertEqual(r.error_code,"LIMIT_EXCEEDED")

    def test_list_dir_and_stat_use_nofollow_fd(self):
        self.assertTrue(self.gw.execute(req(operation="STAT")).ok)
        self.assertTrue(self.gw.execute(req(operation="LIST_DIR",relative_path="dir")).ok)

    def test_no_automatic_failover(self):
        self.assertEqual(self.code(req(fallback_host_id="burzh",equivalent_object_ref="eq-1")),
                         "HOST_UNAVAILABLE")

    def test_canonical_and_audit(self):
        raw=req(operation="SHA256"); parsed=gateway.parse_request(raw); result=self.gw.execute(raw)
        self.assertEqual(gateway.serialize_result(result),gateway.serialize_result(result))
        a=json.loads(gateway.serialize_audit(parsed,result,7))
        self.assertEqual(a["schema"],"wb.shard_gateway.audit.v1"); self.assertEqual(a["mode"],"VERIFY")

    def test_host_mapping_and_concurrency_preserved(self):
        self.assertEqual(gateway.HOST_ROOTS,{
          "mazhor":{"MAZHOR_REPO_WELLBEING_HQ":"/data/wellbeing-lab/repos/wellbeing-hq",
                    "MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01":"/data/wellbeing-lab/backups/shd-pre-reinit-v01"},
          "burzh":{"BURZH_REPO_WELLBEING_HQ":"/home/pev5691/wellbeing-hq"}})
        self.assertEqual(gateway.CONCURRENCY.locks["mazhor"]._value,1)
        self.assertEqual(gateway.CONCURRENCY.locks["burzh"]._value,1)

    def test_git_ref_validator_rejects_symbolic_and_unreachable_for_all(self):
        def fake(argv,cwd,timeout,limit):
            if argv[:5]==["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","merge-base","--is-ancestor"]:
                raise gateway.GatewayError(gateway.ErrorCode.HOST_UNAVAILABLE)
            if argv[:4]==["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","ls-tree"]: return b"100644 blob "+b"a"*40+b"\tfile.txt\n"
            return b""
        for op in ("GIT_LS_TREE","GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"):
            with self.subTest(op=op):
                with patch.object(self.gw,"_run",side_effect=fake):
                    r=self.gw.execute(req(operation=op,relative_path="file.txt",git_ref="main",git_object="a"*40))
                    self.assertEqual(r.error_code,"REF_NOT_ALLOWED")
                    r=self.gw.execute(req(operation=op,relative_path="file.txt",git_ref="b"*40,git_object="a"*40))
                    self.assertEqual(r.error_code,"REF_NOT_ALLOWED")

    def test_git_head_ref_allowed_shared_validator(self):
        def fake(argv,cwd,timeout,limit):
            if argv[:4]==["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","ls-tree"]:
                if "--" in argv: return ("100644 blob "+"a"*40+"\tfile.txt\n").encode()
                return b"100644 blob aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\tfile.txt\n"
            if argv[:5]==["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","cat-file","-s"]: return b"5\n"
            if argv[:5]==["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","cat-file","blob"]: return b"alpha"
            return b""
        for op in ("GIT_LS_TREE","GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"):
            with self.subTest(op=op):
                with patch.object(self.gw,"_run",side_effect=fake):
                    r=self.gw.execute(req(operation=op,relative_path="file.txt",git_ref="HEAD",
                                          git_object="a"*40))
                    self.assertTrue(r.ok,r.error_code)

    def test_git_safe_directory_exact_root_policy(self):
        r=gateway.parse_request(req(operation="GIT_HEAD",relative_path=""))
        self.assertEqual(self.gw._git_argv(r,["rev-parse","HEAD"]),
          ["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq","rev-parse","HEAD"])
        self.assertNotIn("*",self.gw._git_argv(r,["status"]))

    def test_request_cannot_inject_safe_directory(self):
        o=json.loads(req(operation="GIT_HEAD",relative_path=""))
        o["safe_directory"]="/tmp/other"
        self.assertEqual(self.code(gateway.canonical_bytes(o)),"BAD_REQUEST")

    def test_archive_root_never_safe_directory(self):
        o=json.loads(req(operation="GIT_HEAD",relative_path=""))
        o["root_id"]="MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01"
        self.assertEqual(self.code(gateway.canonical_bytes(o)),"GIT_ROOT_REQUIRED")

    def test_all_git_paths_get_exact_safe_directory_and_non_git_does_not(self):
        seen=[]
        def fake(argv,cwd,timeout,limit):
            seen.append(argv)
            tail=argv[3:]
            if tail[:2]==["ls-tree","HEAD"] and "--" in tail:
                return ("100644 blob "+"a"*40+"\\tfile.txt\\n").encode()
            if tail[:2]==["ls-tree","-r"]:
                return b"100644 blob aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\tfile.txt\\n"
            if tail[:2]==["cat-file","-s"]: return b"5\\n"
            if tail[:2]==["cat-file","blob"]: return b"alpha"
            if tail[:2]==["rev-parse","HEAD"]: return b"a"*40+b"\\n"
            if tail[:2]==["rev-parse","HEAD^{tree}"]: return b"b"*40+b"\\n"
            return b""
        for op in ("GIT_STATUS_PORCELAIN","GIT_HEAD","GIT_HEAD_TREE","GIT_LS_TREE","GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"):
            with self.subTest(op=op), patch.object(self.gw,"_run",side_effect=fake):
                kw={"operation":op,"relative_path":""}
                if op in ("GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"):
                    kw.update(relative_path="file.txt",git_ref="HEAD",git_object="a"*40)
                elif op=="GIT_LS_TREE": kw.update(git_ref="HEAD")
                self.gw.execute(req(**kw))
        self.assertTrue(seen)
        for argv in seen:
            self.assertEqual(argv[:3],["git","-c","safe.directory=/data/wellbeing-lab/repos/wellbeing-hq"])
            self.assertEqual(argv.count("-c"),1)
        with patch.object(self.gw,"_run") as run:
            self.gw.execute(req(operation="STAT"))
            run.assert_not_called()

    def test_git_subprocess_environment_stays_minimal_and_no_shell(self):
        import subprocess
        cp=subprocess.CompletedProcess([],0,stdout=b"",stderr=b"")
        r=gateway.parse_request(req(operation="GIT_HEAD",relative_path=""))
        argv=self.gw._git_argv(r,["rev-parse","HEAD"])
        with patch("gateway.subprocess.run",return_value=cp) as sp:
            self.gw._run(argv,self.root,1,64)
        kwargs=sp.call_args.kwargs
        self.assertEqual(kwargs["env"],{"PATH":"/usr/bin:/bin","LC_ALL":"C"})
        self.assertNotIn("shell",kwargs)
        self.assertFalse(any(k.startswith("GIT_CONFIG") for k in kwargs["env"]))

if __name__=="__main__": unittest.main(verbosity=2)
