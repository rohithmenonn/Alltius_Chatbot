import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://www.angelone.in/support"
OUTPUT_DIR = "web_data"
MAX_CHARS = 1500

visited_urls = set()
os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_valid_url(url):
    return url.startswith(BASE_URL) and url not in visited_urls

def get_links(soup, base_url):
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = urljoin(base_url, a_tag['href'])
        if is_valid_url(href):
            links.append(href)
    return links

def chunk_text(text, max_chars=MAX_CHARS):
    lines = text.split("\n")
    chunks, chunk = [], ""
    for line in lines:
        if len(chunk) + len(line) < max_chars:
            chunk += line + "\n"
        else:
            chunks.append(chunk.strip())
            chunk = line + "\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def scrape_page(url):
    print(f"Scraping: {url}")
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
        text = soup.get_text()
        chunks = chunk_text(text)

        filename = urlparse(url).path.strip("/").replace("/", "_") or "index"
        for i, chunk in enumerate(chunks):
            with open(os.path.join(OUTPUT_DIR, f"{filename}_chunk_{i+1}.txt"), "w", encoding="utf-8") as f:
                f.write(chunk)
        return get_links(soup, url)
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return []

def crawl(url):
    queue = [url]
    while queue:
        current = queue.pop(0)
        if is_valid_url(current):
            visited_urls.add(current)
            new_links = scrape_page(current)
            queue.extend(new_links)

if __name__ == "__main__":
    crawl(BASE_URL)
    print("Web scraping complete.")