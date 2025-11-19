from crawler.fetcher import fetch_page
from crawler.parser import extract_links
from crawler.utils import load_json
import os

def run_crawler(max_pages=10):
    links_path = "crawlerTest/data/links.json"
    start_links = load_json(links_path)

    if not start_links:
        print("No links found in data/links.json")
        return

    visited = set()
    queue = list(start_links)
    pages_crawled = 0

    while queue and pages_crawled < max_pages:
        url = queue.pop(0)

        if url in visited:
            continue
        visited.add(url)

        print(f"Crawling ({pages_crawled+1}/{max_pages}): {url}")
        html_path = fetch_page(url)

        if not html_path:
            continue

        pages_crawled += 1


        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()


        new_links = extract_links(html, url)


        for link in new_links:
            if link not in visited:
                queue.append(link)

    print(f"\nCrawling complete. Total pages crawled: {pages_crawled}")


if __name__ == "__main__":
    run_crawler(max_pages=5) 
