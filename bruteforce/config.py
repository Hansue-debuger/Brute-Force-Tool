import argparse

class Config:
    pass

def parse(args):
    p = argparse.ArgumentParser()
    p.add_argument("--target", required=True)
    p.add_argument("--scope", required=True)
    p.add_argument("--wordlist", default="")
    p.add_argument("--mask", default="")
    p.add_argument("--threads", type=int, default=4)
    p.add_argument("--rps", type=int, default=10)
    p.add_argument("--proxies", default="")
    p.add_argument("--output", default="hits.txt")
    p.add_argument("--state", default="session.state")
    ns = p.parse_args(args)
    c = Config()
    for k,v in vars(ns).items():
        setattr(c, k, v)
    return c
