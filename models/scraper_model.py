import requests
from urllib.parse import quote
from bs4 import BeautifulSoup


def extract_domain(url: str) -> str:
    parts = url.split("/")
    return parts[0] + "//" + parts[2]


class ScraperModel:
    def __init__(self, ip: str = "127.0.0.1", port: str = "8888", lang: str = "auto") -> None:
        self.ip = ip
        self.port = port
        self.lang = lang
        self.all_domains = []

    def search_number(self, search_input: str, max_page: int) -> list:
        page_urls = []
        page = 1
        while page < max_page:
            url = f"http://{self.ip}:{self.port}/search?q={quote(search_input)}&category_general=1&pageno={page}&language={self.lang}&time_range=&safesearch=0&theme=simple"
            page_urls.append(url)
            page += 1
        return page_urls

    def get_websites(self, page_urls) -> list:
        self.all_domains = []

        for page_url in page_urls:
            code = requests.get(page_url).text
            soup = BeautifulSoup(code, "html.parser")
            results = soup.find_all("article", class_="result")
            domains = []

            if len(results) > 0:
                for result in results:
                    link_tag = result.find("h3").find("a")
                    if link_tag:
                        link = link_tag["href"]
                        link = extract_domain(link)
                        domains.append(link)

            self.all_domains.extend(domains)
            self.all_domains = list(dict.fromkeys(self.all_domains))

        return self.all_domains