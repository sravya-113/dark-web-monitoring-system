# from bs4 import BeautifulSoup
# import requests

# onion_url = 'http://msydqstlz2kzerdg.onion'  # Ahmia Search

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# response = requests.get(onion_url, proxies=proxies, timeout=10)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Keywords to look for
# keywords = ['password', 'gmail', 'exploit']
# found = []

# # Scan all visible text in common tags
# for tag in soup.find_all(['p', 'a', 'div']):
#     text = tag.get_text().lower()
#     for key in keywords:
#         if key in text:
#             found.append((key, text.strip()))

# # Print results
# print("Potential threats found:")
# for k, t in found:
#     print(f"Keyword: {k} -> {t[:100]}...")


# import requests

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# try:
#     r = requests.get('http://check.torproject.org', proxies=proxies, timeout=10)
#     if 'Congratulations' in r.text:
#         print("✅ Tor is working correctly!")
#     else:
#         print("❌ Tor connection failed.")
# except Exception as e:
#     print("❌ Error connecting via Tor:", e)


# from bs4 import BeautifulSoup
# import requests

# # Ahmia's .onion address (Tor search engine)
# onion_url = 'http://msydqstlz2kzerdg.onion'

# # Route requests through Tor's SOCKS5 proxy
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# # Send request through Tor
# try:
#     response = requests.get(onion_url, proxies=proxies, timeout=10)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Keywords to look for in the HTML
#     keywords = ['password', 'gmail', 'exploit']
#     found = []

#     for tag in soup.find_all(['p', 'a', 'div']):
#         text = tag.get_text().lower()
#         for key in keywords:
#             if key in text:
#                 found.append((key, text.strip()))

#     print("✅ Connected to Ahmia via Tor")
#     print("\n🔍 Potential threats found:")
#     for k, t in found:
#         print(f"Keyword: {k} -> {t[:100]}...")

# except Exception as e:
#     print("❌ Error connecting via Tor:", e)


# from bs4 import BeautifulSoup
# import requests

# # DuckDuckGo Onion URL (reachable via Tor)
# onion_url = 'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion'

# # Use Tor's SOCKS5 proxy
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# try:
#     print("🔌 Connecting via Tor...")
#     response = requests.get(onion_url, proxies=proxies, timeout=15)
#     print("✅ Connected!")

#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Search for keywords
#     keywords = ['password', 'gmail', 'exploit']
#     found = []

#     for tag in soup.find_all(['p', 'a', 'div']):
#         text = tag.get_text().lower()
#         for key in keywords:
#             if key in text:
#                 found.append((key, text.strip()))

#     print("\n🔍 Potential threats found:")
#     for k, t in found:
#         print(f"Keyword: {k} -> {t[:100]}...")

# except Exception as e:
#     print("❌ Error connecting via Tor:", e)



# from bs4 import BeautifulSoup
# import requests
# import csv
# from datetime import datetime
# import os

# onion_url = 'http://msydqstlz2kzerdg.onion'  # Or use another test site

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ['password', 'gmail', 'exploit']
# found = []

# print("🔌 Connecting via Tor...")

# try:
#     response = requests.get(onion_url, proxies=proxies, timeout=10)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for tag in soup.find_all(['p', 'a', 'div']):
#         text = tag.get_text().lower()
#         for key in keywords:
#             if key in text:
#                 found.append((key, text.strip()))

#     print("✅ Connected!")

#     if found:
#         print("🔍 Potential threats found:")
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Create logs directory if it doesn't exist
#         os.makedirs('logs', exist_ok=True)

#         with open('logs/threats.csv', 'a', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             for key, text in found:
#                 writer.writerow([timestamp, key, text[:100]])

#         for k, t in found:
#             print(f"⚠️ Keyword: {k} -> {t[:100]}...")
#     else:
#         print("✅ No keywords found.")

# except Exception as e:
#     print(f"❌ Error connecting or scraping: {e}")



# from bs4 import BeautifulSoup
# import requests
# import csv
# from datetime import datetime
# import os

# # ✅ A working .onion site — DuckDuckGo on Tor
# onion_url = 'http://3g2upl4pq6kufc4m.onion'

# # 🔌 Use Tor SOCKS proxy
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# # 🔍 Keywords to search
# keywords = ['password', 'gmail', 'exploit']
# found = []

# print("🔌 Connecting via Tor...")

# try:
#     # Connect through Tor
#     response = requests.get(onion_url, proxies=proxies, timeout=10)
#     response.raise_for_status()
#     print("✅ Connected!")

#     # Parse HTML using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for tag in soup.find_all(['p', 'a', 'div']):
#         text = tag.get_text().lower()
#         for key in keywords:
#             if key in text:
#                 found.append((key, text.strip()))

#     # 📁 Create logs folder if not exists
#     os.makedirs('logs', exist_ok=True)

#     # 📝 Write to CSV
#     if found:
#         print("🔍 Potential threats found:")
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         with open('logs/threats.csv', 'a', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             for key, text in found:
#                 writer.writerow([timestamp, key, text[:100]])
#                 print(f"⚠️ Keyword: {key} -> {text[:100]}...")
#     else:
#         print("✅ No keywords found.")

# except requests.exceptions.RequestException as e:
#     print(f"❌ Network or request error: {e}")
# except Exception as e:
#     print(f"❌ General error: {e}")


#this is working one 
# from bs4 import BeautifulSoup
# import requests
# import csv
# from datetime import datetime
# import os

# # ✅ Live DuckDuckGo onion URL
# onion_url = 'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion'

# # 🔌 Tor SOCKS proxy config
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ['password', 'gmail', 'exploit']
# found = []

# print("🔌 Connecting via Tor...")

# try:
#     # Connect to the .onion site
#     response = requests.get(onion_url, proxies=proxies, timeout=10)
#     response.raise_for_status()
#     print("✅ Connected!")

#     # Parse with BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for tag in soup.find_all(['p', 'a', 'div']):
#         text = tag.get_text().lower()
#         for key in keywords:
#             if key in text:
#                 found.append((key, text.strip()))

#     os.makedirs('logs', exist_ok=True)

#     if found:
#         print("🔍 Threats found:")
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         with open('logs/threats.csv', 'a', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             for key, text in found:
#                 writer.writerow([timestamp, key, text[:100]])
#                 print(f"⚠️ Keyword: {key} -> {text[:100]}...")
#     else:
#         print("✅ No keywords found.")

# except requests.exceptions.RequestException as e:
#     print(f"❌ Network error: {e}")
# except Exception as e:
#     print(f"❌ General error: {e}")



#this is also working one upto step4
# import requests
# import csv
# import time
# from bs4 import BeautifulSoup

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ["password", "gmail", "exploit", "leak", "credit card"]
# onion_url = 'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion'

# def log_match(timestamp, keyword, match, url):
#     with open("logs/threats.csv", "a", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([timestamp, keyword, match, url])

# def scrape():
#     print("🔌 Connecting via Tor...")
#     try:
#         response = requests.get(onion_url, proxies=proxies, timeout=30)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         text = soup.get_text().lower()

#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#         for keyword in keywords:
#             if keyword in text:
#                 snippet = text[text.index(keyword):text.index(keyword)+60]
#                 print(f"✅ Found keyword '{keyword}' in: {snippet}")
#                 log_match(timestamp, keyword, snippet.strip(), onion_url)
#         print("📦 Done scraping.")
#     except Exception as e:
#         print(f"❌ Error: {e}")

# if __name__ == "__main__":
#     # Create log file with headers if not exists
#     try:
#         with open("logs/threats.csv", "x", newline='', encoding='utf-8') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(["timestamp", "Keyword", "Matched_Text", "URL"])
#     except FileExistsError:
#         pass  # File already exists

#     scrape()




# import requests
# from bs4 import BeautifulSoup
# import csv
# import os
# from datetime import datetime

# proxies = {
#     'http': 'socks5h://127.0.0.1:9050',
#     'https': 'socks5h://127.0.0.1:9050'
# }

# keywords = ["password", "gmail", "exploit", "leak", "credit card", "malware", "keylogger", "hack", "database dump"]

# onion_urls = [
#     "http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion",
#     "http://msydqstlz2kzerdg.onion",
#     # Add more URLs here
# ]

# print("🔌 Connecting via Tor...")

# log_file = "logs/threats.csv"
# os.makedirs("logs", exist_ok=True)

# with open(log_file, mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     if os.stat(log_file).st_size == 0:
#         writer.writerow(["timestamp", "Keyword", "Matched_Text", "URL"])

#     for url in onion_urls:
#         try:
#             response = requests.get(url, proxies=proxies, timeout=30)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             text = soup.get_text()

#             for keyword in keywords:
#                 if keyword.lower() in text.lower():
#                     matched_lines = [line.strip() for line in text.splitlines() if keyword.lower() in line.lower()]
#                     for line in matched_lines:
#                         timestamp = datetime.now().isoformat()
#                         writer.writerow([timestamp, keyword, line[:200], url])  # Limit to 200 chars
#                         print(f"⚠️ Match found: '{keyword}' at {url}")

#         except Exception as e:
#             print(f"❌ Error scraping {url}: {e}")

# print("📦 Done scraping.")



# import requests
# from bs4 import BeautifulSoup
# import csv, os
# from datetime import datetime

# # ✅ Use correct Tor proxy (9150 for Tor Browser, 9050 for standalone Tor)
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# # ✅ Tor Test
# try:
#     test = requests.get("https://check.torproject.org", proxies=proxies, timeout=20)
#     if "Congratulations" in test.text:
#         print("✅ Tor routing confirmed.")
#     else:
#         print("❌ Not using Tor.")
# except Exception as e:
#     print("❌ Tor test failed:", e)

# # ✅ Keywords and URLs
# keywords = ["password", "gmail", "exploit", "leak", "credit card", "malware", "keylogger", "hack", "database dump"]

# onion_urls = [
#     "http://duskgytldkxiuqc6.onion",  # DuckDuckGo
#     "http://zlal32teyptf4tvi.onion",  # ProPublica
# ]

# print("🔌 Connecting via Tor...")

# log_file = "logs/threats.csv"
# os.makedirs("logs", exist_ok=True)

# with open(log_file, mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     if os.stat(log_file).st_size == 0:
#         writer.writerow(["timestamp", "Keyword", "Matched_Text", "URL"])

#     for url in onion_urls:
#         try:
#             response = requests.get(url, proxies=proxies, timeout=30)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             text = soup.get_text()

#             for keyword in keywords:
#                 if keyword.lower() in text.lower():
#                     matched_lines = [line.strip() for line in text.splitlines() if keyword.lower() in line.lower()]
#                     for line in matched_lines:
#                         timestamp = datetime.now().isoformat()
#                         writer.writerow([timestamp, keyword, line[:200], url])
#                         print(f"⚠️ Match found: '{keyword}' at {url}")

#         except requests.exceptions.RequestException as e:
#             print(f"❌ Error scraping {url}: {type(e).__name__}: {e}")

# print("📦 Done scraping.")


# import requests
# from bs4 import BeautifulSoup
# import csv, os
# from datetime import datetime

# # ✅ Use port 9150 if you're using Tor Browser
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# # ✅ Add user-agent to avoid blocking
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
# }

# # ✅ Updated .onion URLs (HTTPS)
# onion_urls = [
#     "https://duskgytldkxiuqc6.onion",   # DuckDuckGo
#     "https://zlal32teyptf4tvi.onion"    # ProPublica
# ]

# keywords = ["password", "gmail", "exploit", "leak", "credit card", "malware", "keylogger", "hack", "database dump"]

# # ✅ Confirm Tor is working
# try:
#     test = requests.get("https://check.torproject.org", proxies=proxies, timeout=20)
#     if "Congratulations" in test.text:
#         print("✅ Tor routing confirmed.")
#     else:
#         print("❌ Tor test failed: not routed via Tor.")
# except Exception as e:
#     print("❌ Tor test connection failed:", e)

# print("🔌 Connecting via Tor...")

# # ✅ Prepare log file
# log_file = "logs/threats.csv"
# os.makedirs("logs", exist_ok=True)

# with open(log_file, mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     if os.stat(log_file).st_size == 0:
#         writer.writerow(["timestamp", "Keyword", "Matched_Text", "URL"])

#     for url in onion_urls:
#         try:
#             response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             text = soup.get_text()

#             for keyword in keywords:
#                 if keyword.lower() in text.lower():
#                     matched_lines = [line.strip() for line in text.splitlines() if keyword.lower() in line.lower()]
#                     for line in matched_lines:
#                         timestamp = datetime.now().isoformat()
#                         writer.writerow([timestamp, keyword, line[:200], url])
#                         print(f"⚠️ Match found: '{keyword}' at {url}")

#         except requests.exceptions.RequestException as e:
#             print(f"❌ Error scraping {url}: {type(e).__name__}: {e}")

# print("📦 Done scraping.")




# import requests
# from bs4 import BeautifulSoup
# import csv, os, re
# from datetime import datetime

# # ✅ Use Tor proxy (adjust to 9050 if you're using the Tor daemon)
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
# }

# # ✅ Keywords to scan for
# keywords = ["password", "gmail", "exploit", "leak", "credit card", "malware", "keylogger", "hack", "database dump"]

# # ✅ Step 1: Scrape `.onion` URLs from Ahmia
# def fetch_onion_links_from_ahmia():
#     print("🌐 Fetching .onion links from Ahmia...")
#     onion_links = set()
#     try:
#         ahmia_url = "https://ahmia.fi/onions/"
#         res = requests.get(ahmia_url, headers=headers, timeout=20)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         text = soup.get_text()
#         found = re.findall(r'http[s]?://[a-zA-Z0-9]{16,56}\.onion', text)
#         onion_links.update(found)
#     except Exception as e:
#         print(f"❌ Failed to fetch from Ahmia: {e}")
#     return list(onion_links)

# # ✅ Step 2: Keyword scan on each .onion site
# def scan_onion_site(url, writer):
#     try:
#         response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         text = soup.get_text()

#         for keyword in keywords:
#             if keyword.lower() in text.lower():
#                 matched_lines = [line.strip() for line in text.splitlines() if keyword.lower() in line.lower()]
#                 for line in matched_lines:
#                     timestamp = datetime.now().isoformat()
#                     writer.writerow([timestamp, keyword, line[:200], url])
#                     print(f"⚠️ Match: '{keyword}' at {url}")

#     except Exception as e:
#         print(f"❌ Error scraping {url}: {type(e).__name__}: {e}")

# # ✅ Step 3: Run the full scraper
# def run_scraper():
#     print("✅ Checking Tor routing...")
#     try:
#         check = requests.get("https://check.torproject.org", proxies=proxies, timeout=10)
#         if "Congratulations" in check.text:
#             print("✅ Tor routing confirmed.")
#         else:
#             print("❌ Not routed over Tor. Check proxy config.")
#             return
#     except Exception as e:
#         print(f"❌ Tor test failed: {e}")
#         return

#     onion_urls = fetch_onion_links_from_ahmia()
#     print(f"🔍 Found {len(onion_urls)} .onion links to scan.")

#     if not onion_urls:
#         print("⚠️ No valid .onion URLs found. Exiting.")
#         return

#     os.makedirs("logs", exist_ok=True)
#     log_file = "logs/threats.csv"

#     with open(log_file, mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         if os.stat(log_file).st_size == 0:
#             writer.writerow(["timestamp", "Keyword", "Matched_Text", "URL"])

#         for url in onion_urls:
#             print(f"🔎 Scanning: {url}")
#             scan_onion_site(url, writer)

#     print("📦 Done scanning.")

# # ✅ Start the scraper
# if __name__ == "__main__":
#     run_scraper()


# import requests
# from bs4 import BeautifulSoup

# # .onion sites (safe & public)
# onion_urls = [
#     "https://duskgytldkxiuqc6.onion",   # DuckDuckGo
#     "https://zlal32teyptf4tvi.onion"    # ProPublica
# ]

# proxies = {
#     "http": "socks5h://127.0.0.1:9150",
#     "https": "socks5h://127.0.0.1:9150"
# }

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }

# print("✅ Checking Tor routing...")

# try:
#     r = requests.get("https://check.torproject.org", proxies=proxies, timeout=10)
#     if "Congratulations" in r.text:
#         print("🟢 Tor is working!")
#     else:
#         print("⚠️ Tor test failed.")
# except Exception as e:
#     print(f"❌ Tor test failed: {e}")

# print("🔌 Connecting via Tor...")

# for url in onion_urls:
#     try:
#         r = requests.get(url, proxies=proxies, headers=headers, timeout=15)
#         soup = BeautifulSoup(r.text, "html.parser")
#         title = soup.title.string.strip() if soup.title else "No title found"
#         print(f"✅ {url} → {title}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# print("📦 Done scraping.")



# import requests

# proxies = {
#     'http': 'socks5h://127.0.0.1:9050',
#     'https': 'socks5h://127.0.0.1:9050'
# }

# session = requests.Session()
# session.proxies = proxies

# TOR_SITES = [
#     "http://msydqstlz2kzerdg.onion",  # Ahmia
#     "http://3g2upl4pq6kufc4m.onion",  # DuckDuckGo
# ]

# print("✅ Checking Tor routing...")

# try:
#     tor_check = session.get("https://check.torproject.org", timeout=10)
#     if "Congratulations" in tor_check.text:
#         print("🟢 Tor is working!")
#     else:
#         print("⚠️ Tor connected, but not routed properly.")
# except Exception as e:
#     print("❌ Tor test failed:", e)

# print("🔌 Connecting via Tor...")

# for site in TOR_SITES:
#     try:
#         print(f"🔍 Trying {site}")
#         response = session.get(site, timeout=15)
#         response.raise_for_status()
#         print(f"✅ Success: {site}\n")
#         print(response.text[:300])
#     except Exception as e:
#         print(f"❌ Error scraping {site}: {e}")

# print("📦 Done scraping.")



# import requests

# # Set proxies to match Tor Browser (which uses port 9150)
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# def check_tor():
#     print("✅ Checking Tor routing...")
#     try:
#         res = requests.get('https://check.torproject.org', proxies=proxies, timeout=10)
#         if "Congratulations" in res.text:
#             print("🟢 Tor routing confirmed.")
#         else:
#             print("⚠️ Not routed via Tor.")
#     except Exception as e:
#         print(f"❌ Tor test failed: {e}")

# def scrape_onion(url):
#     print(f"🔍 Trying {url}")
#     try:
#         res = requests.get(url, proxies=proxies, timeout=15)
#         print(f"✅ Success: {url[:30]}... | Status Code: {res.status_code}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# if __name__ == "__main__":
#     check_tor()
#     print("🔌 Connecting via Tor...")
#     scrape_onion('http://msydqstlz2kzerdg.onion')     # ProPublica
#     scrape_onion('http://3g2upl4pq6kufc4m.onion')     # DuckDuckGo
#     print("📦 Done scraping.")



# import requests

# # Working Tor proxy
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# def check_tor():
#     print("✅ Checking Tor routing...")
#     try:
#         res = requests.get('https://check.torproject.org', proxies=proxies, timeout=10)
#         if "Congratulations" in res.text:
#             print("🟢 Tor routing confirmed.")
#         else:
#             print("⚠️ Not routed via Tor.")
#     except Exception as e:
#         print(f"❌ Tor test failed: {e}")

# def scrape_onion(url):
#     print(f"🔍 Trying {url}")
#     try:
#         res = requests.get(url, proxies=proxies, timeout=20)
#         print(f"✅ Success! {url[:50]} | Status: {res.status_code}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# if __name__ == "__main__":
#     check_tor()
#     print("🔌 Connecting via Tor...")
#     scrape_onion('http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion')
#     scrape_onion('http://y6xjgkgwj47us5ca.onion')  # Intercept
#     print("📦 Done scraping.")




#this is workinggg completely
# import requests

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# def scrape_onion(url):
#     print(f"🔍 Trying {url}")
#     try:
#         res = requests.get(url, proxies=proxies, timeout=20)
#         print(f"✅ Success! {url[:50]} | Status: {res.status_code}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# if __name__ == "__main__":
#     print("🔌 Connecting via Tor...")
#     scrape_onion('http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion')
#     scrape_onion('http://protonirockerxow.onion')
#     scrape_onion('http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion')
#     print("📦 Done scraping.")




#this is also working coretly and perfectly and its true
# import requests

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ["password", "exploit", "gmail", "credit card", "bitcoin", "leak", "credentials", "hacked"]

# def scrape_onion(url):
#     print(f"🔍 Trying {url}")
#     try:
#         res = requests.get(url, proxies=proxies, timeout=20)
#         if res.status_code == 200:
#             print(f"✅ Success! {url[:50]} | Status: {res.status_code}")
#             content = res.text.lower()
#             matches = [k for k in keywords if k in content]
#             if matches:
#                 print(f"🚨 Threat Detected on {url} → Keywords Found: {matches}")
#                 with open("threats_found.txt", "a", encoding='utf-8') as f:
#                     f.write(f"{url} - FOUND: {matches}\n")
#             else:
#                 print(f"🟢 No threats found on {url}")
#         else:
#             print(f"⚠️ Non-200 response: {res.status_code}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# if __name__ == "__main__":
#     print("🔌 Connecting via Tor...")
#     onion_sites = [
#         'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
#         'http://protonirockerxow.onion',
#         'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion',
#         'http://dreadykbxjv4gxpa.onion',
#         'http://hss3uro2hsxfogfq.onion'
#     ]
#     for site in onion_sites:
#         scrape_onion(site)
#     print("📦 Done scraping.")



# import requests
# from datetime import datetime
# import csv

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ["password", "exploit", "gmail", "credit card", "bitcoin", "leak", "credentials", "hacked"]

# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
# }

# def scrape_onion(url):
#     print(f"🔍 Trying {url}")
#     try:
#         res = requests.get(url, proxies=proxies, headers=headers, timeout=20)
#         if res.status_code == 200:
#             print(f"✅ Success! {url[:50]} | Status: {res.status_code}")
#             content = res.text.lower()
#             found = False
#             with open("threats.csv", "a", newline='', encoding='utf-8') as f:
#                 writer = csv.writer(f)
#                 for keyword in keywords:
#                     if keyword in content:
#                         # extract lines containing keyword for context
#                         lines = [line.strip() for line in content.splitlines() if keyword in line]
#                         for line in lines:
#                             timestamp = datetime.now().isoformat()
#                             writer.writerow([timestamp, keyword, line[:200], url])
#                             print(f"🚨 Threat Detected: '{keyword}' → {line[:100]}...")
#                             found = True
#             if not found:
#                 print(f"🟢 No threats found on {url}")
#         else:
#             print(f"⚠️ Non-200 response: {res.status_code}")
#     except Exception as e:
#         print(f"❌ Error scraping {url}: {e}")

# if __name__ == "__main__":
#     # Write CSV header if file is empty or missing
#     import os
#     if not os.path.exists("threats.csv") or os.path.getsize("threats.csv") == 0:
#         with open("threats.csv", "w", newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

#     print("🔌 Connecting via Tor...")
#     onion_sites = [
#         'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
#         'http://protonirockerxow.onion',
#         'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion',
#         'http://dreadykbxjv4gxpa.onion',
#         'http://hss3uro2hsxfogfq.onion'
#     ]
#     for site in onion_sites:
#         scrape_onion(site)
#     print("📦 Done scraping.")



#this is perfectly working and correct also and it si truw for the project
# import requests
# from datetime import datetime
# import csv
# import time

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ["password", "exploit", "gmail", "credit card", "bitcoin", "leak", "credentials", "hacked"]

# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
# }

# def scrape_onion(url, max_retries=3):
#     print(f"🔍 Trying {url}")
#     for attempt in range(1, max_retries + 1):
#         try:
#             res = requests.get(url, proxies=proxies, headers=headers, timeout=20)
#             if res.status_code == 200:
#                 print(f"✅ Success! {url} | Status: {res.status_code}")
#                 content = res.text.lower()
#                 found = False
#                 with open("threats.csv", "a", newline='', encoding='utf-8') as f:
#                     writer = csv.writer(f)
#                     for keyword in keywords:
#                         if keyword in content:
#                             lines = [line.strip() for line in content.splitlines() if keyword in line]
#                             for line in lines:
#                                 timestamp = datetime.now().isoformat()
#                                 writer.writerow([timestamp, keyword, line[:200], url])
#                                 print(f"🚨 Threat Detected: '{keyword}' → {line[:100]}...")
#                                 found = True
#                 if not found:
#                     print(f"🟢 No threats found on {url}")
#                 return  # success, no need to retry
#             else:
#                 print(f"⚠️ Non-200 response: {res.status_code}")
#                 return
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Attempt {attempt} failed for {url}: {e}")
#             if attempt < max_retries:
#                 print("⏳ Retrying...")
#                 time.sleep(5)  # wait before retrying
#             else:
#                 print("❌ Max retries reached, moving on.")
#                 return

# if __name__ == "__main__":
#     import os
#     if not os.path.exists("threats.csv") or os.path.getsize("threats.csv") == 0:
#         with open("threats.csv", "w", newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

#     print("🔌 Connecting via Tor...")
#     onion_sites = [
#         'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
#         'http://protonirockerxow.onion',
#         'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion',
#         'http://dreadykbxjv4gxpa.onion',
#         'http://hss3uro2hsxfogfq.onion'
#     ]
#     for site in onion_sites:
#         scrape_onion(site)
#     print("📦 Done scraping.")




# import requests
# from datetime import datetime
# import csv
# import time

# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# keywords = ["password", "exploit", "gmail", "credit card", "bitcoin", "leak", "credentials", "hacked"]

# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
# }

# def scrape_onion(url, max_retries=3):
#     print(f"🔍 Trying {url}")
#     for attempt in range(1, max_retries + 1):
#         try:
#             res = requests.get(url, proxies=proxies, headers=headers, timeout=20)
#             if res.status_code == 200:
#                 print(f"✅ Success! {url} | Status: {res.status_code}")
#                 content = res.text.lower()
#                 found = False
#                 with open("threats.csv", "a", newline='', encoding='utf-8') as f:
#                     writer = csv.writer(f)
#                     for keyword in keywords:
#                         if keyword in content:
#                             lines = [line.strip() for line in content.splitlines() if keyword in line]
#                             for line in lines:
#                                 timestamp = datetime.now().isoformat()
#                                 writer.writerow([timestamp, keyword, line[:200], url])
#                                 print(f"🚨 Threat Detected: '{keyword}' → {line[:100]}...")
#                                 found = True
#                 if not found:
#                     print(f"🟢 No threats found on {url}")
#                 return  # success, no need to retry
#             else:
#                 print(f"⚠️ Non-200 response: {res.status_code}")
#                 return
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Attempt {attempt} failed for {url}: {e}")
#             if attempt < max_retries:
#                 print("⏳ Retrying...")
#                 time.sleep(5)  # wait before retrying
#             else:
#                 print("❌ Max retries reached, moving on.")
#                 return
# import csv
# from collections import Counter

# def print_summary_report(filename='threats.csv'):
#     counts = Counter()
#     with open(filename, newline='', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             counts[row['Keyword']] += 1
#     print("\n=== Threat Keywords Summary ===")
#     for keyword, count in counts.most_common():
#         print(f"{keyword}: {count} hits")

# if __name__ == "__main__":
#     import os
#     if not os.path.exists("threats.csv") or os.path.getsize("threats.csv") == 0:
#         with open("threats.csv", "w", newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

#     print("🔌 Connecting via Tor...")
#     onion_sites = [
#         'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',
#         'http://protonirockerxow.onion',
#         'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion',
#         'http://dreadykbxjv4gxpa.onion',
#         'http://hss3uro2hsxfogfq.onion'
#     ]
#     for site in onion_sites:
#         scrape_onion(site)
#     print("📦 Done scraping.")
#     print_summary_report()




#this is also a working one time please 
# import requests
# from datetime import datetime
# import csv
# import time
# import os

# # Tor SOCKS5 proxy configuration
# proxies = {
#     'http': 'socks5h://127.0.0.1:9150',
#     'https': 'socks5h://127.0.0.1:9150'
# }

# # Keywords to search for on the dark web pages
# keywords = [
#     "password", "exploit", "gmail", "credit card",
#     "bitcoin", "leak", "credentials", "hacked"
# ]

# # Custom headers to mimic a browser
# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; DarkWebThreatMonitor/1.0)'
# }

# # Function to scrape and scan an onion site
# def scrape_onion(url, max_retries=3):
#     print(f"🔍 Trying {url}")
#     for attempt in range(1, max_retries + 1):
#         try:
#             res = requests.get(url, proxies=proxies, headers=headers, timeout=30)
#             if res.status_code == 200:
#                 print(f"✅ Success! {url} | Status: {res.status_code}")
#                 content = res.text.lower()
#                 found = False
#                 with open("threats.csv", "a", newline='', encoding='utf-8') as f:
#                     writer = csv.writer(f)
#                     for keyword in keywords:
#                         if keyword in content:
#                             lines = [
#                                 line.strip() for line in content.splitlines() if keyword in line
#                             ]
#                             for line in lines:
#                                 timestamp = datetime.now().isoformat()
#                                 writer.writerow([timestamp, keyword, line[:200], url])
#                                 print(f"🚨 Threat Detected: '{keyword}' → {line[:100]}...")
#                                 found = True
#                 if not found:
#                     print(f"🟢 No threats found on {url}")
#                 return
#             else:
#                 print(f"⚠️ Non-200 response: {res.status_code} from {url}")
#                 return
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Attempt {attempt} failed for {url}: {e}")
#             if attempt < max_retries:
#                 print("⏳ Retrying in 5 seconds...")
#                 time.sleep(5)
#             else:
#                 print("❌ Max retries reached. Moving on.")
#                 return

# # Main execution block
# if __name__ == "__main__":
#     # Create CSV if it doesn't exist
#     if not os.path.exists("threats.csv") or os.path.getsize("threats.csv") == 0:
#         with open("threats.csv", "w", newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(["Timestamp", "Keyword", "Matched_Text", "URL"])

#     print("🔌 Connecting via Tor network...")

#     # List of onion sites to scan
#     onion_sites = [
#         'http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion',  # DuckDuckGo
#         'http://protonirockerxow.onion',                                        # ProtonMail
#         'http://sdolvtlfj2xjvxkozy4npkhpwncehbcokhffhkhskn3pfjlhqbtptwid.onion', # Possible market
#         'http://dreadykbxjv4gxpa.onion',                                        # Dread forum
#         'http://hss3uro2hsxfogfq.onion'                                         # The Hidden Wiki
#     ]

#     for site in onion_sites:
#         scrape_onion(site)

#     print("📦 Scraping completed. Results saved in threats.csv")





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




