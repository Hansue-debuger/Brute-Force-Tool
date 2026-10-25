import sys
from bruteforce.config import parse
from bruteforce.auth import authorize
from bruteforce.engine import Engine

def main():
    cfg = parse(sys.argv[1:])
    authorize(cfg.target, cfg.scope)
    Engine(cfg).run()

if __name__ == "__main__":
    main()
