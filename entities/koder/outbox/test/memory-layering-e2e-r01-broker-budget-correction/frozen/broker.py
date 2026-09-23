#!/usr/bin/env python3
from pathlib import Path
import json, os, socket, sys

BASE=Path("/home/shd/ml-e2e-r01-admission")
PACKAGE=BASE/"supervisor/package"
CONFIG=BASE/"supervisor/broker-config.json"
SOCK=BASE/"broker-runtime/semantic.sock"
LOG=BASE/"evidence/broker-readiness-log.json"

cfg=json.loads(CONFIG.read_text())
allowed={x["path"]:x for x in cfg["allowlist"]}
denied=set(cfg["denied_exact"])
max_reads=cfg["max_reads"]
max_bytes=cfg["max_bytes"]

try: SOCK.unlink()
except FileNotFoundError: pass
SOCK.parent.mkdir(parents=True,exist_ok=True)
server=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
server.bind(str(SOCK))
os.chmod(SOCK,0o600)
server.listen(8)

reads=0
semantic_bytes=0
wire_bytes=0
events=[]

def reply(conn,obj):
    global wire_bytes
    raw=(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n").encode()
    wire_bytes += len(raw)
    conn.sendall(raw)

while len(events) < cfg["sentinel_request_budget"]:
    conn,_=server.accept()
    raw=conn.recv(8192)
    wire_bytes += len(raw)
    reads += 1
    event={"read_index":reads}
    try:
        req=json.loads(raw)
        if type(req) is not dict or set(req)!={"op","locator"} or req["op"]!="read" or type(req["locator"]) is not str:
            event["decision"]="DENY_BAD_REQUEST"
            reply(conn,{"status":"DENY","reason":"BAD_REQUEST","reads":reads,"semantic_bytes":semantic_bytes})
        else:
            loc=req["locator"]
            event["locator"]=loc
            if reads>max_reads:
                event["decision"]="DENY_READ_LIMIT"
                reply(conn,{"status":"DENY","reason":"READ_LIMIT","reads":reads,"semantic_bytes":semantic_bytes})
            elif loc in denied or loc.startswith("verifier-private/") or loc.startswith("provenance/") or loc.startswith("schemas/"):
                event["decision"]="DENY_FORBIDDEN_LOCATOR"
                reply(conn,{"status":"DENY","reason":"FORBIDDEN_LOCATOR","reads":reads,"semantic_bytes":semantic_bytes})
            elif loc not in allowed:
                event["decision"]="DENY_UNKNOWN_LOCATOR"
                reply(conn,{"status":"DENY","reason":"UNKNOWN_LOCATOR","reads":reads,"semantic_bytes":semantic_bytes})
            else:
                p=(PACKAGE/loc).resolve()
                if not str(p).startswith(str(PACKAGE.resolve())+os.sep) or not p.is_file():
                    event["decision"]="DENY_MISSING_EXACT_EVIDENCE"
                    reply(conn,{"status":"DENY","reason":"MISSING_EXACT_EVIDENCE","reads":reads,"semantic_bytes":semantic_bytes})
                else:
                    data=p.read_bytes()
                    import hashlib, base64
                    if hashlib.sha256(data).hexdigest()!=allowed[loc]["sha256"]:
                        event["decision"]="DENY_HASH_MISMATCH"
                        reply(conn,{"status":"DENY","reason":"HASH_MISMATCH","reads":reads,"semantic_bytes":semantic_bytes})
                    elif semantic_bytes+len(data)>max_bytes:
                        event["decision"]="DENY_BYTE_LIMIT"
                        reply(conn,{"status":"DENY","reason":"BYTE_LIMIT","reads":reads,"semantic_bytes":semantic_bytes})
                    else:
                        semantic_bytes += len(data)
                        event["decision"]="ALLOW"
                        event["bytes"]=len(data)
                        reply(conn,{"status":"OK","locator":loc,"sha256":allowed[loc]["sha256"],
                                    "bytes":len(data),"payload_b64":base64.b64encode(data).decode(),
                                    "reads":reads,"semantic_bytes":semantic_bytes})
    except Exception as e:
        event["decision"]="DENY_PARSE_OR_INTERNAL"
        event["error_type"]=type(e).__name__
        reply(conn,{"status":"DENY","reason":"PARSE_OR_INTERNAL","reads":reads,"semantic_bytes":semantic_bytes})
    conn.close()
    events.append(event)

server.close()
try: SOCK.unlink()
except FileNotFoundError: pass
LOG.write_text(json.dumps({"schema":"mltest.semantic-broker-readiness.r01",
 "reads":reads,"semantic_bytes":semantic_bytes,"wire_bytes":wire_bytes,
 "max_reads":max_reads,"max_bytes":max_bytes,"events":events},
 sort_keys=True,separators=(",",":"))+"\n")
