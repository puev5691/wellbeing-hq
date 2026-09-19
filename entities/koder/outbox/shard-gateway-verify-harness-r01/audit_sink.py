from __future__ import annotations
from pathlib import Path
import errno
import json
import os
import stat

MAX_AUDIT_RECORD_BYTES=16384

class AuditSinkError(RuntimeError): pass

def canonical(v):
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")

def append_record(path:Path,record:dict)->None:
    data=canonical(record)+b"\n"
    if len(data)>MAX_AUDIT_RECORD_BYTES: raise AuditSinkError("AUDIT_RECORD_TOO_LARGE")
    flags=os.O_WRONLY|os.O_APPEND|os.O_CREAT|os.O_NOFOLLOW
    try: fd=os.open(path,flags,0o600)
    except OSError: raise AuditSinkError("AUDIT_OPEN_FAILED") from None
    try:
        st=os.fstat(fd)
        if not stat.S_ISREG(st.st_mode): raise AuditSinkError("AUDIT_NOT_REGULAR")
        total=0
        while total<len(data):
            try: n=os.write(fd,data[total:])
            except OSError: raise AuditSinkError("AUDIT_WRITE_FAILED") from None
            if type(n) is not int or n<=0: raise AuditSinkError("AUDIT_PARTIAL_WRITE")
            total+=n
        if total!=len(data): raise AuditSinkError("AUDIT_PARTIAL_WRITE")
        try: os.fsync(fd)
        except OSError: raise AuditSinkError("AUDIT_FSYNC_FAILED") from None
    finally:
        try: os.close(fd)
        except OSError: pass
