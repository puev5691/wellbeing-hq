#!/usr/bin/env python3
from __future__ import annotations
import hashlib, html, json, re, shutil
from pathlib import Path

INPUT_BLOBS = {
    "route-map.json": "94c79cb035387986e8147a6ea52d41b3e7e30be5",
    "content-eligibility-ledger.json": "c8dbac045b51cf2f5315b0b29ae74f5eea393246",
    "route-presentation-delta.json": "47648448fa632f45e79fb4a7d5b0a1028bc6d774",
    "presentation-spec.md": "7ab2d9555b57499ee457ce2abc1142586020742b",
}
BANNER = "NON-PRODUCTION PREVIEW — НЕ ПУБЛИЧНЫЙ РЕЛИЗ"
BADGES = {
    "draft": "Черновик",
    "working": "Рабочий материал",
    "working skeleton": "Рабочий каркас",
    "skeleton": "Каркас",
    "candidate": "Кандидат",
}
HUMAN_COPY = {
    "public-info-portal-current": "Разрабатываемый информационный портал; сейчас доступен только непроизводственный слой представления для проверки.",
    "entity-ai-resource-boosters": "Направление разработки, проходящее отдельные технические проверки перед ограниченным live-исполнением.",
    "telegram-facilitator-direction": "Направление разработки; запуск ожидает отдельной технической подготовки с необходимыми полномочиями.",
    "entity-ai-resource-boosters-live-gate": "До ограниченного live-вызова остаются проверки доступа к провайдеру и учётной записи, разрешённой модели, защищённого доступа и отдельного разрешения на вызов.",
    "telegram-phase1b-host-runtime-gate": "Запуск ожидает отдельной технической подготовки с необходимыми полномочиями.",
    "achievement-stage-b-baseline": "Сформирована ограниченная непроизводственная базовая модель информационного входа.",
    "achievement-static-preview-contract": "Принят контракт представления статического preview.",
    "achievement-static-preview-v03-e1": "Закрыта узкая повторная проверка Static Preview v0.3 E1.",
    "achievement-info-entry-r2-shd-reverify": "Пройдена межслойная повторная проверка информационного входа r2.",
}
NAV = [
    ("/", "Главная"), ("/project/", "О проекте"), ("/developments/", "Текущие разработки"),
    ("/achievements/", "Проверенные рубежи"), ("/status/gates/", "Ожидающие проверки и ограничения"),
    ("/participate/", "Участие"), ("/cooperation/", "Кооперация"), ("/knowledge/", "База знаний"),
    ("/publications/", "Публикации")
]
STYLE = """html{font-family:system-ui,-apple-system,sans-serif;background:#f7f7f5;color:#202020}body{margin:0}
header{background:#fff;border-bottom:1px solid #ddd;padding:1rem 5vw;position:sticky;top:0}
.banner{font-weight:800;border:2px solid #111;padding:.6rem;margin-bottom:.8rem;background:#fff2c7}
nav a{margin-right:1rem;color:#222}main{max-width:960px;margin:auto;padding:2rem 5vw}
.card{background:#fff;border:1px solid #ddd;border-radius:10px;padding:1rem;margin:1rem 0}
.badge{display:inline-block;border:1px solid #555;border-radius:999px;padding:.15rem .55rem;margin:.15rem;font-size:.85rem}
.stale{font-weight:700}.empty{padding:1rem;border-left:4px solid #777;background:#fff}
.provenance{margin-top:1rem;color:#555}.provenance code{word-break:break-all}
.source-body{background:#fff;padding:1rem;border:1px solid #ddd}.source-body h1,.source-body h2{line-height:1.2}
footer{max-width:960px;margin:2rem auto;padding:1rem 5vw;color:#666}"""

class BuildError(RuntimeError): pass

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_pinned(inputs: Path, name: str) -> bytes:
    data=(inputs/name).read_bytes()
    if git_blob(data)!=INPUT_BLOBS[name]:
        raise BuildError("SOURCE_IDENTITY_MISMATCH:"+name)
    return data

def route_file(root: Path, route: str) -> Path:
    if not route.startswith("/") or ".." in route or "//" in route:
        raise BuildError("BAD_ROUTE:"+route)
    if route=="/": return root/"index.html"
    return root/route.strip("/")/"index.html"

def simple_markdown(text: str) -> str:
    out=[]; in_list=False
    for raw in text.splitlines():
        line=raw.rstrip()
        if not line:
            if in_list: out.append("</ul>"); in_list=False
            continue
        if line.startswith("# "):
            if in_list: out.append("</ul>"); in_list=False
            out.append("<h2>"+html.escape(line[2:].strip())+"</h2>")
        elif line.startswith("## "):
            if in_list: out.append("</ul>"); in_list=False
            out.append("<h3>"+html.escape(line[3:].strip())+"</h3>")
        elif line.startswith("- "):
            if not in_list: out.append("<ul>"); in_list=True
            out.append("<li>"+html.escape(line[2:].strip())+"</li>")
        else:
            if in_list: out.append("</ul>"); in_list=False
            out.append("<p>"+html.escape(line)+"</p>")
    if in_list: out.append("</ul>")
    return "\n".join(out)

def provenance(entry: dict) -> str:
    fields=[
        ("Источник", entry["source_repo"]+":"+entry["source_path"]),
        ("Commit", entry["source_commit"]), ("Blob", entry["source_blob"]),
        ("Literal status", entry["literal_status"]), ("Release", entry["release_state"]),
        ("Representation", entry["representation_state"]), ("Public ready", str(entry["public_ready"]).lower())
    ]
    body="".join(f"<dt>{html.escape(k)}</dt><dd><code>{html.escape(v)}</code></dd>" for k,v in fields)
    return '<details class="provenance"><summary>Технические сведения и происхождение</summary><dl>'+body+"</dl></details>"

def entry_card(entry: dict, body: str|None) -> str:
    labels=[]
    if entry["literal_status"] in BADGES: labels.append(BADGES[entry["literal_status"]])
    if "stale" in entry["stale_state"].lower(): labels.append("Актуальность не подтверждена")
    labels_html="".join('<span class="badge">'+html.escape(x)+"</span>" for x in labels)
    if body is not None:
        heading = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), entry["id"])
        content='<div class="source-body">'+simple_markdown(body)+"</div>"
    else:
        heading=entry["id"].replace("-"," ")
        copy=HUMAN_COPY.get(entry["id"])
        if copy is None:
            if entry["semantic_bucket"]=="superseded": copy="Исторический материал; заменён более новой принятой версией."
            else: copy="Доступна только проверяемая метаинформация; публичное тело в эту версию не включено."
        content="<p>"+html.escape(copy)+"</p>"
    return '<article class="card"><h2>'+html.escape(heading)+"</h2>"+labels_html+content+provenance(entry)+"</article>"

def shell(title: str, content: str) -> str:
    nav="".join(f'<a href="{html.escape(r)}">{html.escape(t)}</a>' for r,t in NAV)
    return '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="/assets/style.css"></head><body><header><div class="banner">'+BANNER+'</div><nav>'+nav+'</nav></header><main><h1>'+html.escape(title)+'</h1>'+content+'</main><footer>Непроизводственный локальный preview. Публичный выпуск не разрешён.</footer></body></html>\n'

def build(inputs: Path, out: Path) -> dict:
    route_map=json.loads(load_pinned(inputs,"route-map.json"))
    ledger=json.loads(load_pinned(inputs,"content-eligibility-ledger.json"))
    delta=json.loads(load_pinned(inputs,"route-presentation-delta.json"))
    load_pinned(inputs,"presentation-spec.md")
    if route_map.get("public_ready") is not False or ledger.get("public_ready") is not False or ledger.get("state_database") is not False or delta.get("public_ready") is not False:
        raise BuildError("PUBLIC_READY_OR_STATE_DB_MISMATCH")
    entries={e["id"]:e for e in ledger["entries"]}
    for e in entries.values():
        if e["public_body_in_r01_preview"]:
            if e["source_mode"]!="curated-content" or not e["source_path"].startswith("docs/public/"):
                raise BuildError("BODY_ADMISSION_MISMATCH:"+e["id"])
            body=(inputs/"content"/(e["id"]+".md")).read_bytes()
            if git_blob(body)!=e["source_blob"]:
                raise BuildError("SOURCE_IDENTITY_MISMATCH:"+e["id"])
        else:
            if (inputs/"content"/(e["id"]+".md")).exists():
                raise BuildError("METADATA_BODY_PRESENT:"+e["id"])
    for r in route_map["routes"]:
        for sid in r["source_ids"]:
            if sid not in entries: raise BuildError("UNKNOWN_SOURCE:"+sid)
    overrides={x["route"]:x for x in delta["routes"]}
    if out.exists(): shutil.rmtree(out)
    (out/"assets").mkdir(parents=True)
    (out/"assets"/"style.css").write_text(STYLE,encoding="utf-8",newline="\n")

    all_routes={r["route"] for r in route_map["routes"]}|{e["portal_route"] for e in entries.values()}
    route_meta={r["route"]:r for r in route_map["routes"]}
    page_routes=[]
    for route in sorted(all_routes):
        rmeta=route_meta.get(route)
        title=(overrides.get(route) or {}).get("public_title") or (rmeta["title"] if rmeta else None)
        direct=[e for e in entries.values() if e["portal_route"]==route]
        source_ids=(rmeta["source_ids"] if rmeta else [e["id"] for e in direct])
        if title is None:
            if direct:
                bodyfile=inputs/"content"/(direct[0]["id"]+".md")
                if bodyfile.exists():
                    txt=bodyfile.read_text(encoding="utf-8")
                    title=next((l[2:].strip() for l in txt.splitlines() if l.startswith("# ")) , direct[0]["id"].replace("-"," "))
                else: title=direct[0]["id"].replace("-"," ")
            else: title=route
        blocks=[]
        empty=(overrides.get(route) or {}).get("empty_state")
        if empty: blocks.append('<div class="empty">'+html.escape(empty)+"</div>")
        # exact ordered source mapping from route-map first; individual page uses direct source
        for sid in source_ids:
            e=entries[sid]
            body_path=inputs/"content"/(sid+".md")
            body=body_path.read_text(encoding="utf-8") if body_path.exists() and e["portal_route"]==route else None
            blocks.append(entry_card(e,body))
            if e["portal_route"]!=route:
                blocks.append('<p><a href="'+html.escape(e["portal_route"])+'">Открыть отдельную карточку источника</a></p>')
        if not source_ids and not empty:
            blocks.append('<div class="empty">Для этого маршрута в текущей сборке нет допущенного содержимого.</div>')
        target=route_file(out,route);target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(shell(title,"".join(blocks)),encoding="utf-8",newline="\n")
        page_routes.append({"route":route,"file":target.relative_to(out).as_posix(),"source_ids":source_ids,"title":title})
    routes_obj={"schema":"portal-static-routes-r01","public_ready":False,"routes":page_routes}
    (out/"routes.json").write_text(json.dumps(routes_obj,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8",newline="\n")
    files={}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name!="build-manifest.json":
            data=p.read_bytes();files[p.relative_to(out).as_posix()]={"sha256":sha256(data),"bytes":len(data)}
    manifest={
        "schema":"portal-static-build-manifest-r01","deterministic":True,"public_ready":False,
        "deployment":"none","state_database":False,
        "inputs":{"route_map_blob":INPUT_BLOBS["route-map.json"],"ledger_blob":INPUT_BLOBS["content-eligibility-ledger.json"],"presentation_delta_blob":INPUT_BLOBS["route-presentation-delta.json"],"presentation_spec_blob":INPUT_BLOBS["presentation-spec.md"]},
        "routes_count":len(page_routes),"files":files
    }
    (out/"build-manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8",newline="\n")
    return manifest

def tree_digest(root:Path)->str:
    h=hashlib.sha256()
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        rel=p.relative_to(root).as_posix().encode();data=p.read_bytes()
        h.update(len(rel).to_bytes(4,"big"));h.update(rel);h.update(len(data).to_bytes(8,"big"));h.update(data)
    return h.hexdigest()

if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument("--inputs",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args();m=build(a.inputs,a.out);print(json.dumps({"verdict":"PASS_BUILD","routes":m["routes_count"],"tree_digest":tree_digest(a.out)},sort_keys=True))
