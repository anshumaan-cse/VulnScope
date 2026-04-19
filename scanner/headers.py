import requests
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Security headers configuration
SECURITY_HEADERS = {
    "Content-Security-Policy": {
        "risk": "HIGH",
        "weight": 2,
        "info": "Prevents XSS and data injection attacks"
    },
    "Strict-Transport-Security": {
        "risk": "HIGH",
        "weight": 2,
        "info": "Forces HTTPS to prevent MITM attacks"
    },
    "X-Frame-Options": {
        "risk": "MEDIUM",
        "weight": 1,
        "info": "Prevents clickjacking attacks"
    },
    "X-Content-Type-Options": {
        "risk": "MEDIUM",
        "weight": 1,
        "info": "Prevents MIME sniffing"
    },
    "Referrer-Policy": {
        "risk": "LOW",
        "weight": 1,
        "info": "Controls referrer information leakage"
    },
    "Permissions-Policy": {
        "risk": "LOW",
        "weight": 1,
        "info": "Restricts browser features"
    }
}


def check_headers(url):
    result = {
        "url": url,
        "present": [],
        "missing": [],
        "score": 0,
        "max_score": sum(h["weight"] for h in SECURITY_HEADERS.values())
    }

    try:
        print(Fore.CYAN + f"\n[+] Scanning: {url}")

        # Send request
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "VulnScope-Scanner/1.0"}
        )

        headers = response.headers

        print(Fore.YELLOW + "\n[+] Security Headers Analysis:\n")

        for header, details in SECURITY_HEADERS.items():
            if header in headers:
                print(Fore.GREEN + f"[OK] {header}")
                result["present"].append(header)
                result["score"] += details["weight"]
            else:
                color = Fore.RED if details["risk"] == "HIGH" else Fore.YELLOW
                print(color + f"[MISSING] {header} ({details['risk']})")
                print(f"   ↳ {details['info']}")
                result["missing"].append(header)

        # Calculate percentage score
        percentage = (result["score"] / result["max_score"]) * 100

        print(Fore.CYAN + f"\n[+] Security Score: {percentage:.1f}%")

        if percentage > 85:
            print(Fore.GREEN + "✔ Strong security posture")
        elif percentage > 60:
            print(Fore.YELLOW + "⚠ Moderate security")
        else:
            print(Fore.RED + "✘ Weak security")

        return result

    except requests.exceptions.RequestException:
        print(Fore.RED + "[ERROR] Unable to connect to target")
        return None
