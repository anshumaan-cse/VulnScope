import requests
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)


def check_headers(url):
    try:
        print(Fore.CYAN + f"\n[+] Scanning: {url}\n")

        # Send request with timeout + custom User-Agent
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "VulnScope-Scanner/1.0"}
        )

        headers = response.headers

        # Basic info
        print(f"Status Code: {response.status_code}")
        print(f"Server: {headers.get('Server', 'Unknown')}\n")

        print(Fore.YELLOW + "\n[+] Security Headers Analysis:\n")

        # Security headers dictionary
        security_headers = {
            "Content-Security-Policy": {
                "risk": "HIGH",
                "info": "Prevents XSS and data injection attacks"
            },
            "Strict-Transport-Security": {
                "risk": "HIGH",
                "info": "Forces HTTPS to prevent MITM attacks"
            },
            "X-Frame-Options": {
                "risk": "MEDIUM",
                "info": "Prevents clickjacking attacks"
            },
            "X-Content-Type-Options": {
                "risk": "LOW",
                "info": "Prevents MIME sniffing"
            },
            "Referrer-Policy": {
                "risk": "LOW",
                "info": "Controls referrer information leakage"
            },
            "Permissions-Policy": {
                "risk": "MEDIUM",
                "info": "Restricts browser features"
            }
        }

        score = 0
        total = len(security_headers)

        # Check headers
        for header, details in security_headers.items():
            if header in headers:
                print(Fore.GREEN + f"[OK] {header} present")
                score += 1
            else:
                color = Fore.RED if details["risk"] == "HIGH" else Fore.YELLOW
                print(
                    color +
                    f"[MISSING] {header} ({details['risk']} RISK)\n"
                    f"   ↳ {details['info']}"
                )

        # Score summary
        print("\n" + Fore.CYAN + f"[+] Security Score: {score}/{total}")

        if score == total:
            print(Fore.GREEN + "[✔] Excellent security configuration")
        elif score >= total // 2:
            print(Fore.YELLOW + "[!] Moderate security - needs improvement")
        else:
            print(Fore.RED + "[✘] Poor security configuration")

    except requests.exceptions.RequestException:
        print(Fore.RED + "[ERROR] Unable to connect to target")
