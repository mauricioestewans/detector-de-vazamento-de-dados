import requests
from bs4 import BeautifulSoup
from utils.regex_patterns import EMAIL_REGEX, CPF_REGEX

GIST_URL = "https://gist.github.com/discover"

def get_recent_gists(limit=3):
    r = requests.get(GIST_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    gists = soup.select("div.d-flex > a")[:limit]
    links = ["https://gist.github.com" + a["href"] for a in gists]
    return links

def extract_data_from_gist(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        content_blocks = soup.select("table.highlight td.blob-code")

        content = "\n".join([block.get_text() for block in content_blocks])
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
