import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque
import time

def simple_crawler(start_url, max_pages):
    queue = deque([start_url])
    visited = set()

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        print(f"Crawling: {url}")
        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")


            for a in soup.find_all("a", href=True):
                full = urljoin(url, a["href"])
                if full not in visited:
                    queue.append(full)

            time.sleep(1)

        except Exception as e:
            print("Error:", e)

    return visited

visited_pages = simple_crawler("https://terraria.fandom.com/wiki/DPS_Meter", 10)
print("Crawled pages:", visited_pages)
