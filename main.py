import argparse
from scanner.headers import check_headers


def main():
    parser = argparse.ArgumentParser(
        description="VulnScope - HTTP Security Header Analyzer"
    )

    parser.add_argument("--url", help="Target URL to scan")

    args = parser.parse_args()

    if not args.url:
        print("[!] Please provide a URL using --url")
        print("Example: python main.py --url https://example.com")
        return

    url = args.url.strip()

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    result = check_headers(url)

    if result:
        print("\n--- Summary ---")
        print(f"Target URL     : {result.get('url')}")
        print(f"Headers Present: {len(result.get('present', []))}")
        print(f"Headers Missing: {len(result.get('missing', []))}")
        print("-" * 30)


if __name__ == "__main__":
    main()
