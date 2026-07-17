# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_website_contents(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No Title"

    for tag in soup(["script","style","nav","footer","header","img","input"]):
        tag.decompose()

    content = []

    for tag in soup.find_all(["h1","h2","h3","p"]):
        txt = tag.get_text(" ", strip=True)

        if txt:
            content.append(txt)

    text = "\n".join(content)

    MAX_CHARS = 8000
    text = text[:MAX_CHARS]

    return f"""
Title: {title}

Page contents:
{text}
"""