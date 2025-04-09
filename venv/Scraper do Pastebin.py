import requests
from bs4 import BeautifulSoup
from utils.regex_patterns import EMAIL_REGEX, CPF_REGEX

PASTEBIN_URL = "https://pastebin.com"

def get_recent_pastes(limit=5):
    r = requests.get(PASTEBIN_URL)
    soup = BeautifulSoup(r.text, 'html.parser')

    pastes = soup.select("table.maintable a")
    links = [PASTEBIN_URL + a["href"] for a in pastes[:limit]]
    return links

def extract_data_from_paste(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        content = soup.select_one("#paste_code").get_text()

        emails = EMAIL_REGEX.findall(content)
        cpfs = CPF_REGEX.findall(content)

        return {
            "url": url,
            "emails": emails,
            "cpfs": cpfs
        }

    except Exception as e:
        print(f"[!] Erro em {url}: {e}")
        return None
