import os
from dotenv import load_dotenv
from models.scraper_model import ScraperModel
from models.security_model import SecurityModel

load_dotenv()

class VerifyController:
    def __init__(self, search) -> None:
        self.search = search
        self.ip = os.getenv("SEARXNG_IP") or None
        self.port = os.getenv("SEARXNG_PORT") or None
        self.lang = os.getenv("SEARXNG_LANGUAGE") or None
        self.max_pages = int(os.getenv("SEARXNG_PAGES") or 10)

    def find_domains(self) -> None:
        sc = ScraperModel(self.ip, self.port, self.lang)
        domains = sc.search_number(self.search, self.max_pages)
        all_domains = sc.get_websites(domains)
        sm = SecurityModel(all_domains)
        sm.verify_security()