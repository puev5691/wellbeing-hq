"""Node-local fixed-IP HTTPS observation adapter (not executed by tests).

The supervisor must independently attest node identity and authorize any live
network use. This adapter never handles credentials or private requests.
"""

import ipaddress
import socket
import ssl

from router import Observation, Outcome, TARGET


def probe_fixed_ip(ip: str, *, timeout_seconds: float = 10.0) -> Observation:
    """Connect to a caller-admitted IPv4, preserving chatgpt.com TLS/HTTP identity.

    Caller is responsible for ensuring `ip` came from an admitted immutable
    profile. No DNS lookup or response body read occurs here.
    """
    # Refuse a hostname before socket.create_connection can invoke DNS.
    try:
        if type(ip) is not str or str(ipaddress.IPv4Address(ip)) != ip:
            return Observation(Outcome.TARGET_IP_FAILURE)
    except ipaddress.AddressValueError:
        return Observation(Outcome.TARGET_IP_FAILURE)
    if not 0 < timeout_seconds <= 20:
        return Observation(Outcome.TARGET_IP_FAILURE)
    raw = None
    try:
        raw = socket.create_connection((ip, 443), timeout=timeout_seconds)
        raw.settimeout(timeout_seconds)
        context = ssl.create_default_context()
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED
        with context.wrap_socket(raw, server_hostname=TARGET) as tls:
            raw = None
            tls.sendall(b"HEAD / HTTP/1.1\r\nHost: chatgpt.com\r\nUser-Agent: wbnp-fixed-ip-health-r01\r\nConnection: close\r\n\r\n")
            line = bytearray()
            while len(line) < 256:
                byte = tls.recv(1)
                if not byte or byte == b"\n":
                    break
                line.extend(byte)
            if not line.endswith(b"\r"):
                return Observation(Outcome.TARGET_IP_FAILURE)
            pieces = bytes(line[:-1]).split(b" ", 2)
            if len(pieces) < 2 or pieces[0] not in (b"HTTP/1.0", b"HTTP/1.1"):
                return Observation(Outcome.TARGET_IP_FAILURE)
            try:
                status = int(pieces[1])
            except ValueError:
                return Observation(Outcome.TARGET_IP_FAILURE)
            if not 100 <= status <= 599:
                return Observation(Outcome.TARGET_IP_FAILURE)
            return Observation(Outcome.HTTP_APPLICATION_RESPONSE, status)
    except ssl.SSLCertVerificationError:
        return Observation(Outcome.TLS_CERTIFICATE_FAILURE)
    except (OSError, ssl.SSLError):
        return Observation(Outcome.TARGET_IP_FAILURE)
    finally:
        if raw is not None:
            raw.close()
