from utils.regex_patterns import EMAIL_REGEX, CPF_REGEX
from utils.tor_session import get_tor_session
from bs4 import BeautifulSoup

def scrape_dark_forum(url, limit_pages=1):
    session = get_tor_session()
    resultados = []

    for i in range(1, limit_pages + 1):
        try:
            page_url = f"{url}?page={i}"
            r = session.get(page_url, timeout=20)
            soup = BeautifulSoup(r.text, 'html.parser')

            posts = soup.find_all("div", class_="post-content")
            for post in posts:
                content = post.get_text()
                emails = EMAIL_REGEX.findall(content)
                cpfs = CPF_REGEX.findall(content)

                if emails or cpfs:
                    resultados.append({
                        "url": page_url,
                        "emails": emails,
                        "cpfs": cpfs
                    })

        except Exception as e:
            print(f"[!] Erro ao acessar {url}: {e}")

    return resultados
