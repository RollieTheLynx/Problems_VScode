import requests
from bs4 import BeautifulSoup

'''
Сайт Caica генерирует оглавление Java скриптом, проще сохранить table с ссылками в браузере.

'''

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# ==========================
# CONFIGURATION
# ==========================

HTML_FILE = "C:\\Users\\Mike\\Documents\\Python_Scripts\\Problems_VScode\\Parsing\\caica_table.html"          # Local HTML file
BASE_URL = "https://www.caica.ru/common/AirInter/validaip/html/" # Base URL of the site
OUTPUT_DIR = "downloads"          # Where PDFs will be saved

# ==========================
# HELPERS
# ==========================

def sanitize_filename(name):
    """Remove invalid filename characters."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def download_file(url, save_path):
    """Download a file from URL to save_path."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    if os.path.exists(save_path):
        print(f"Already exists: {save_path}")
        return

    print(f"Downloading: {url}")
    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# ==========================
# MAIN LOGIC
# ==========================

def main():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    target_div = soup.find("div", id=5025)

    if not target_div:
        print(f"Div with id={5025} not found.")
        return

    links = target_div.find_all("a", href=True)

    for link in links:
        href = link["href"]

        # Only process direct PDF links
        if not href.lower().endswith(".pdf"):
            continue

        title = link.get("title") or link.text.strip()
        title = sanitize_filename(title)

        # Build absolute URL
        file_url = urljoin(BASE_URL, href)

        # Preserve subfolder structure from href
        parsed_path = urlparse(href).path
        relative_path = parsed_path.lstrip("./")  # remove leading ../ or ./

        # Remove leading ../ segments
        while relative_path.startswith("../"):
            relative_path = relative_path[3:]

        folder = os.path.dirname(relative_path)
        filename = os.path.basename(relative_path)

        # Use title as filename but keep original extension
        extension = os.path.splitext(filename)[1]
        final_filename = f"{title}{extension}"

        save_path = os.path.join(OUTPUT_DIR, folder, final_filename)

        download_file(file_url, save_path)

    print("Done.")

if __name__ == "__main__":
    main()