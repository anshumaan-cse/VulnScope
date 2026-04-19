import argparse
import json
from scanner.headers import check_headers


def load_urls(file_path):
    try:
        with open(file_path, "r") as f:
            return [u.strip() for u in f if u.strip()]
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return []


def main():
    parser = argparse.ArgumentParser(
        description="VulnScope - HTTP Security Header Analyzer"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="Scan a single URL")
    group.add_argument("--file", help="Scan URLs from file")

    parser.add_argument("--output", default="report.json",
                        help="Output report file")

    args = parser.parse_args()

    # Get URLs
    if args.url:
        urls = [args.url.strip()]
    else:
        urls = load_urls(args.file)

    if not urls:
        print("[!] No valid URLs")
        return

    # Normalize URLs
    urls = [
        u if u.startswith(("http://", "https://")) else "http://" + u
        for u in urls
    ]

    print("=" * 50)
    print("VulnScope - Security Scanner")
    print("=" * 50)

    results = []

    for url in urls:
        result = check_headers(url)
        if result:
            results.append(result)

    # Save report
    if results:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)

        print(f"\n[+] Report saved as: {args.output}")
    else:
        print("[!] No results to save")


if __name__ == "__main__":
    main()
