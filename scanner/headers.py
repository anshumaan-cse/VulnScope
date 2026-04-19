import requests
from colorama import Fore, Style, init

init()

def check_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers 

        print(f"\nStatus Code: {response.status_code}")
        print(f"Server: {headers.get('Server', 'Unknown')}\n")

        print("\n[+] Security Headers Check:\n")

        important_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        for header in important_headers:
            if header in headers:
                print(Fore.GREEN + f"[✓] {header} is present" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"[X] {header} is missing" + Style.RESET_ALL)

    except Exception as e:
        print(f"Error: {e}")
