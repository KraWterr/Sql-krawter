import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

class Injector:
    def error_based_sqli_scan(self, url):
        print("\033[95m╭───────────────────────╮\033[0m")
        print("\033[95m│    SQL Injection Taraması  │\033[0m")
        print("\033[95m╰───────────────────────╯\033[0m")
        print("\033[94mTaranıyor...\033[0m")

        payloads = ["'"]  # Sadece ' karakteri payload olarak kullanılacak
        check = re.compile("Bilinmeyen Hata|Incorrect syntax|Databaseye bağlanılamıyor|Databasede hata oluştu|Syntax error|Hata oluştu|An error occured|Error MySQL Database|SQL hatası|You have an error|in your syntax|Bilinmeyen karakter|Unclosed.+mark|unterminated.+quote|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)

        with ThreadPoolExecutor(max_workers=10) as executor:
            # Ana URL için işlem başlat
            future = executor.submit(self.scan, url, payloads, check)
            future.result()

            # Sayfada bulunan tüm bağlantıları bul ve işleme sok
            soup = self.get_soup(url)
            if soup:
                links = self.extract_links(url, soup)
                for link in links:
                    future = executor.submit(self.scan, link, payloads, check)
                    future.result()

    def scan(self, url, payloads, check):
        for payload in payloads:
            test_url = url + payload
            try:
                response = requests.get(test_url, timeout=5)
                if check.search(response.text):
                    print("\033[92m╭───────────────────────╮\033[0m")
                    print("\033[92m│   Enjeksiyon Tespit Edildi   │\033[0m")
                    print("\033[92m╰───────────────────────╯\033[0m")
                    print("\033[92mURL:\033[0m", url)
                    print("\033[92mPayload:\033[0m", payload)
                else:
                    print("\033[91m╭───────────────────────╮\033[0m")
                    print("\033[91m│   Enjeksiyon Bulunamadı   │\033[0m")
                    print("\033[91m╰───────────────────────╯\033[0m")
                    print("\033[91mURL:\033[0m", url)
                    print("\033[91mPayload:\033[0m", payload)
            except requests.RequestException:
                print("\033[91m╭───────────────────────╮\033[0m")
                print("\033[91m│    Bağlantı Hatası    │\033[0m")
                print("\033[91m╰───────────────────────╯\033[0m")
                print("\033[91mBağlanılamadı:\033[0m", test_url)

    def get_soup(self, url):
        try:
            response = requests.get(url)
            return BeautifulSoup(response.content, "html.parser")
        except requests.RequestException:
            print("\033[91mHTML alınamadı:\033[0m", url)
            return None

    def extract_links(self, base_url, soup):
        links = []
        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(base_url, link["href"])
            links.append(absolute_url)
        return links

def main():
    injector = Injector()
    print("\033[95m╭───────────────────────────────╮\033[0m")
    print("\033[95m│      SQL Injection Taraması    │\033[0m")
    print("\033[95m╰───────────────────────────────╯\033[0m")
    print("\033[94mBu kod bir yazılımcı tarafından oluşturulmuştur. Daha fazla bilgi için Telegram'da @weertyyyy ile iletişime geçin.\033[0m")
    url = input("\033[94mLütfen test edilecek ana URL'yi girin:\033[0m ")
    injector.error_based_sqli_scan(url)

if __name__ == "__main__":
    main()