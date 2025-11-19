from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, "lxml")

    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        full_url = urljoin(base_url, href)
        links.append(full_url)

    return links
