import requests
from datetime import datetime
import csv
import time
import os
from collections import Counter

# Tor SOCKS5 proxy configuration
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

# Keywords to search for on the dark web pages
keywords = [
    "password", "exploit", "gmail", "credit card",
    "bitcoin", "leak", "credentials", "hacked"
]

# Custom headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
}

# Function to scrape and scan an onion site
def scrape_onion(url, max_retries=3):
    print(f"🔍 Trying {url}")
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.get(url, proxies=proxies, headers=headers, timeout=30)
            if res.status_code == 200:
                print(f"✅ Success! {url} | Status: {res.status_code}")
                content = res.text.lower()
                found = False
                with open("threats.csv", "a", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    for keyword in keywords:
                        if keyword in content:
                            lines = [
                                line.strip() for line in content.splitlines() if keyword in line
                            ]
                            for line in lines:
                                timestamp = datetime.now().isoformat()
                                writer.writerow([timestamp, keyword, line[:200], url])
                                print(f"🚨 Threat Detected: '{keyword}' → {line[:100]}...")
                                found = True
                if not found:
                    print(f"🟢 No threats found on {url}")
                return
            else:
                print(f"⚠️ Non-200 response: {res.status_code} from {url}")
                return
        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt} failed for {url}: {e}")
            if attempt < max_retries:
                print("⏳ Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("❌ Max retries reached. Moving on.")
                return

# Function to print keyword summary after scraping
def print_summary_report(filename='threats.csv'):
    counts = Counter()
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                keyword = row.get('Keyword')
                if keyword:
                    counts[keyword.lower()] += 1
        print("\n=== Threat Keywords Summary ===")
        if counts:
            for keyword, count in counts.most_common():
                print(f"{keyword}: {count} hits")
        else:
            print("No threats found in this run.")
    except FileNotFoundError:
        print("⚠️ threats.csv not found.")

# Main execution block
if __name__ == "__main__":
    # Create CSV if it doesn't exist or is empty
    if not os.path.exists("threats.csv") or os.path.getsize("threats.csv") == 0:
        with open("threats.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

    print("🔌 Connecting via Tor network...")

    # List of onion sites to scan
    onion_sites = [
        'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',  # DuckDuckGo
        'http://protonirockerxow.onion',                                        # ProtonMail
        'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion', # Possible market
        'http://dreadykbxjv4gxpa.onion',                                        # Dread forum
        'http://hss3uro2hsxfogfq.onion'                                         # The Hidden Wiki
    ]

    for site in onion_sites:
        scrape_onion(site)

    print("📦 Scraping completed. Results saved in threats.csv")

    # Show keyword summary
    print_summary_report()




