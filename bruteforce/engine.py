import asyncio

class Engine:
    def __init__(self, cfg):
        self.cfg = cfg

    async def handler(self, candidate, state):
        from .protocol import HTTPProtocol
        proto = HTTPProtocol(self.cfg.target)
        ok, info = await proto.try_password("admin", candidate)
        state["completed"] = state.get("completed", 0) + 1
        if ok:
            print("HIT:", candidate)
            with open(self.cfg.output, "a") as f:
                f.write(candidate + "\n")

    async def run_async(self):
        from .perm import expand
        from .worker import WorkerPool
        from .state import load, save
        st = load(self.cfg.state)
        cands = list(expand(self.cfg.mask)) if self.cfg.mask else []
        start = st.get("completed", 0)
        cands = cands[start:]
        pool = WorkerPool(self.cfg.threads, lambda c: self.handler(c, st), self.cfg.rps)
        await pool.run(cands)
        save(self.cfg.state, {"target": self.cfg.target, "completed": st.get("completed",0), "total": len(cands)+start})
        print("done; checkpoint saved")

    def run(self):
        asyncio.run(self.run_async())
