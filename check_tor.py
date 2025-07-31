import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

r = requests.get('http://check.torproject.org', proxies=proxies)
print("Tor status:", 'Yes' if 'Congratulations' in r.text else 'No')
