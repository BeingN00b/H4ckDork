import argparse
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm

from modules.google_search import search_google
from modules.crawler import crawl_urls
from modules.exporter import export_results
from modules.utils import save_checkpoint, load_checkpoint, setup_logging

def setup_browser(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def load_dorks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="DorkScanner - Search engine dorking tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-f", "--file", required=True, help="Path to dork list")
    parser.add_argument("--resume", action="store_true", help="Resume from previous session")
    parser.add_argument("--crawl", action="store_true", help="Crawl URLs found")
    parser.add_argument("--html", action="store_true", help="Export HTML report")
    parser.add_argument("--csv", action="store_true", help="Export CSV report")
    parser.add_argument("--markdown", action="store_true", help="Export Markdown report")
    parser.add_argument("--delay", type=int, default=5, help="Delay between dorks (seconds)")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")

    args = parser.parse_args()

    setup_logging()

    driver = setup_browser(headless=args.headless)

    dorks = load_dorks(args.file)
    results = []
    checkpoint_file = "checkpoint.json"
    start_index = 0

    if args.resume and os.path.exists(checkpoint_file):
        saved = load_checkpoint(checkpoint_file)
        results = saved.get("results", [])
        start_index = saved.get("index", 0)

    for i in tqdm(range(start_index, len(dorks)), desc="Scanning dorks"):
        dork = dorks[i]
        try:
            res = search_google(driver, dork, args.domain, i)
            results.append(res)

            if args.crawl:
                crawl_urls(res["urls"])

            save_checkpoint("checkpoint.json", results, i + 1)
            time.sleep(args.delay)
        except Exception as e:
            print(f"[!] Error on dork {i}: {e}")
            continue

    export_results(results, html=args.html, csv=args.csv, markdown=args.markdown)

    driver.quit()
    print("[✔] Scanning completed.")

if __name__ == "__main__":
    main()