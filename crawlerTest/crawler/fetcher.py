import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(ROOT_DIR, "data", "crawled")


def fetch_page(url, save_dir=DATA_DIR):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        os.makedirs(save_dir, exist_ok=True)

        filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
        filepath = os.path.join(save_dir, f"{filename}.html")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Saved: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None
