import requests
from datetime import datetime
import csv
import time
import os
from collections import Counter

# === Configuration ===
TOR_PROXY = 'socks5h://127.0.0.1:9150'
THREAT_FILE = 'threats.csv'
MAX_LINE_LEN = 200

proxies = {
    'http': TOR_PROXY,
    'https': TOR_PROXY
}

keywords = [
    "password", "exploit", "gmail", "credit card",
    "bitcoin", "leak", "credentials", "hacked"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
}

# === Functions ===

def scrape_onion(url, max_retries=3):
    print(f"\n🔍 Scanning: {url}")
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.get(url, proxies=proxies, headers=headers, timeout=30)
            if res.status_code == 200:
                print(f"✅ Success: {url} [HTTP {res.status_code}]")
                content = res.text.lower()
                found = False
                with open(THREAT_FILE, "a", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    for keyword in keywords:
                        if keyword in content:
                            lines = [
                                line.strip() for line in content.splitlines() if keyword in line
                            ]
                            for line in lines:
                                timestamp = datetime.now().isoformat()
                                truncated_line = line[:MAX_LINE_LEN]
                                writer.writerow([timestamp, keyword, truncated_line, url])
                                print(f"🚨 Detected: '{keyword}' → {truncated_line[:100]}...")
                                found = True
                if not found:
                    print(f"🟢 No keywords found.")
                return
            else:
                print(f"⚠️ HTTP {res.status_code} from {url}")
                if attempt < max_retries:
                    print("🔁 Retrying...")
                    time.sleep(5)
                else:
                    print("❌ Giving up after max retries.")
                return
        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                print("⏳ Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("❌ Max retries reached. Moving on.")
                return

def print_summary_report(filename=THREAT_FILE):
    counts = Counter()
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                keyword = row.get('Keyword')
                if keyword:
                    counts[keyword.lower()] += 1
        print("\n=== 🔍 Threat Keywords Summary ===")
        if counts:
            for keyword, count in counts.most_common():
                print(f"🔸 {keyword}: {count} hit(s)")
        else:
            print("✅ No threats detected.")
    except FileNotFoundError:
        print("⚠️ threats.csv not found. No data to summarize.")

# === Main Program ===

if __name__ == "__main__":
    if not os.path.exists(THREAT_FILE) or os.path.getsize(THREAT_FILE) == 0:
        with open(THREAT_FILE, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

    print("🔌 Connecting to the dark web via Tor...")

    onion_sites = [
        'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
        'http://protonirockerxow.onion',
        'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion',
        'http://dreadykbxjv4gxpa.onion',
        'http://hss3uro2hsxfogfq.onion'
    ]

    for site in onion_sites:
        scrape_onion(site)

    print("\n📦 Scraping complete. Results saved to threats.csv.")
    print_summary_report()

