import asyncio, aiohttp, requests, re
from views.checker_view import CheckerView
from views.count_view import CountView

def extract_routes(url, body):
    hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', body)
    actions = re.findall(r'<form[^>]+action=["\']([^"\']+)["\']', body)
    js = re.findall(r'["\'](/[a-zA-Z0-9_\-/]+)["\']', body)
    redirs = re.findall(r'window\.location(?:\.href|\.replace|\.assign)\s*[\(=]\s*["\']([^"\']+)["\']', body)
    all_routes = hrefs + actions + js + redirs
    internal = [f"{url}{route}".replace("//", "/") for route in all_routes if route.startswith("/")]
    external = [route for route in all_routes if route.startswith("http")]
    return list(set(internal + external))

def extract_scripts(domain, code) -> list:
    results = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', code, re.IGNORECASE)
    internal = [f"{domain}/{s}".replace("//", "/") for s in results if not s.startswith("http")]
    external = [s for s in results if s.startswith("http")]
    return list(set(internal + external))

def verify_captcha(code) -> int:
    return len(re.findall(r"captcha|recaptcha|hcaptcha|g-recaptcha|h-captcha", code, re.IGNORECASE))

def verify_cloudflare(code) -> int:
    return len(re.findall(r"cf-turnstile|just a moment|challenge-platform|cloudflare challenge|cf_chl_opt|cf_chl_prog|cf-challenge|managed-challenge|cf_chl_f_tk|jschl-answer|jschl_vc|jschl_answer|ray id|cf-spinner|challenge-form|cloudflare ray id|cf-please-wait|cf-error-overview|cf-wrapper|cf-browser-verification", code, re.IGNORECASE))

class SecurityModel:
    def __init__(self, websites) -> None:
        self.websites = websites
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    async def fetch_route(self, session, website, route, visited):
        if route in visited:
            return 0, []
        visited.add(route)
        try:
            async with session.get(route) as response:
                r = await response.text()
        except Exception:
            return 0, []
        cc = verify_captcha(r)
        cd = verify_cloudflare(r)
        script_routes = extract_scripts(website, r)
        code_routes = extract_routes(website, r)
        return cc + cd, script_routes + code_routes

    async def process_website(self, website):
        show_response = CheckerView()
        visited = set()
        queue = []
        domain_quantity = 0

        try:
            r_checkout = requests.get(f"{website}/checkout", timeout=(10,15), headers=self.headers)
            if r_checkout.status_code != 200:
                show_response.route_response(website, r_checkout.status_code, False)
                return 0
            checkout_html = r_checkout.text
            domain_quantity += verify_captcha(checkout_html)
            domain_quantity += verify_cloudflare(checkout_html)
            queue.extend(extract_scripts(website, checkout_html))
            queue.extend(extract_routes(website, checkout_html))
        except requests.exceptions.RequestException:
            return 0

        try:
            r_home = requests.get(website, timeout=(10,15), headers=self.headers).text
        except requests.exceptions.RequestException:
            return 0

        queue.extend(extract_scripts(website, r_home))
        queue.extend(extract_routes(website, r_home))

        if not queue:
            show_response.highsecurity_response(website, 0, False)
            return 0

        timeout = aiohttp.ClientTimeout(connect=10, total=15)
        async with aiohttp.ClientSession(headers=self.headers, timeout=timeout) as session:
            while queue:
                chunk = queue[:20]
                queue = queue[20:]
                tasks = [self.fetch_route(session, website, route, visited) for route in chunk]
                results = await asyncio.gather(*tasks)
                for count, new_routes in results:
                    domain_quantity += count
                    for r in new_routes:
                        if r not in visited:
                            queue.append(r)

        if domain_quantity == 0:
            show_response.security_response(website, domain_quantity, True)
            return 1
        else:
            show_response.security_response(website, domain_quantity, False)
            return 0

    def verify_security(self) -> None:
        cntv = CountView(self.websites)
        cntv.count_domains()
        num_passed = 0

        async def run_all():
            nonlocal num_passed
            tasks = [self.process_website(website) for website in self.websites]
            results = await asyncio.gather(*tasks)
            num_passed = sum(results)

        asyncio.run(run_all())
        cntv.count_passed(num_passed)