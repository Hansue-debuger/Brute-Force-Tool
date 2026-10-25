CHARSETS = {"?l": "abcdefghijklmnopqrstuvwxyz", "?u": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "?d": "0123456789", "?s": "!@#$%^&*"}

def expand(mask):
    # returns generator of strings for simple single-charset masks like ?l?l?d
    import itertools
    groups = []
    i = 0
    while i < len(mask):
        tok = mask[i:i+2]
        if tok in CHARSETS:
            groups.append(CHARSETS[tok]); i += 2
        else:
            groups.append(tok); i += 1
    for combo in itertools.product(*[g if isinstance(g, str) and len(g)>1 else [g] for g in groups]):
        yield "".join(combo)
