def stream(path, fn):
    with open(path, buffering=1024*1024) as f:
        for line in f:
            if not fn(line.rstrip("\n")):
                break
