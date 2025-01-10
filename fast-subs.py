import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import pyfiglet

ascii_art = pyfiglet.figlet_format("fast-subs")
print(ascii_art)

domain = 'DOMAIN FOR SUBDOMAIN ENUMERATION : '

# Read subdomains from the file
with open('subdomains-10000.txt') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

# Lock for thread-safe operations
lock = threading.Lock()

# Function to check subdomain
def check_subdomain(subdomain):
    url = f'https://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain: ", url)
        with lock:
            discovered_subdomains.append(url)

# Use ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_subdomain, subdomains)

# Write discovered subdomains to a file
with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
# Output results
print(f"Results are saved as '{domain}_subdomains.txt'")
print(f"Total subdomains found: {len(discovered_subdomains)}")
