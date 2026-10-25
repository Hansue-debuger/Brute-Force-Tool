import hashlib

def authorize(target, scope_file):
    with open(scope_file) as f:
        targets = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
    if target not in targets:
        raise SystemExit(f"authorization denied: {target} not in scope")

def verify_scope_hash(path, expected):
    h = hashlib.sha256(open(path,'rb').read()).hexdigest()
    if h != expected:
        raise ValueError("scope hash mismatch")
