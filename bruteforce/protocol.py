import asyncio, random, urllib.request, urllib.parse

UAS = ["Mozilla/5.0", "curl/8.0", "BruteForce/1.0"]

class HTTPProtocol:
    def __init__(self, url, proxies=None, success_rules=None):
        self.url = url
        self.proxies = proxies or []
        self.rules = success_rules or {}

    async def try_password(self, user, password):
        data = urllib.parse.urlencode({"username": user, "password": password}).encode()
        proxy = random.choice(self.proxies) if self.proxies else None
        opener = urllib.request.build_opener()
        if proxy:
            opener.add_handler(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
        req = urllib.request.Request(self.url, data=data, headers={"User-Agent": random.choice(UAS)})
        loop = asyncio.get_event_loop()
        try:
            resp = await loop.run_in_executor(None, lambda: opener.open(req, timeout=10))
            body = resp.read().decode(errors="ignore")
            status = resp.getcode()
        except Exception as e:
            return False, str(e)
        from .fingerprint import is_success
        ok = is_success(body, status, self.rules)
        return ok, body
