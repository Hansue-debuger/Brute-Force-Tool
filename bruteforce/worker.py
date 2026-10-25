import asyncio

class WorkerPool:
    def __init__(self, n, handler, rps):
        self.n = n
        self.handler = handler
        self.sem = asyncio.Semaphore(n)
        self.delay = 1.0 / max(1, rps)

    async def run(self, candidates):
        async def worker(c):
            async with self.sem:
                await self.handler(c)
                await asyncio.sleep(self.delay)
        await asyncio.gather(*(worker(c) for c in candidates))
