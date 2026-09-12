import html, json
from pathlib import Path
from validator import load_schema, validate_object
base=Path(__file__).resolve().parent
schema=load_schema(base)
rows=[]
for p in sorted((base/"fixtures").glob("*.json")):
    obj=json.loads(p.read_text(encoding="utf-8")); r=validate_object(obj,schema)
    rows.append((p.name,obj["title"],r["public_ready"],", ".join(r["errors"]) or "PASS"))
parts=["<!doctype html><meta charset='utf-8'><title>Bounded info-entry pilot r1</title>",
"<h1>Bounded information-entry pilot preview r1</h1>",
"<p><strong>NON-PRODUCTION.</strong> Rendering does not upgrade any gate.</p>",
"<table border='1'><tr><th>fixture</th><th>title</th><th>public_ready</th><th>validation</th></tr>"]
for name,title,ready,errors in rows:
    parts.append(f"<tr><td>{html.escape(name)}</td><td>{html.escape(title)}</td><td>{str(ready).lower()}</td><td>{html.escape(errors)}</td></tr>")
parts.append("</table>")
(base/"preview.html").write_text("\n".join(parts)+"\n",encoding="utf-8")
