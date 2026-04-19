import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from scanner.headers import check_headers


def load_urls(file_path):
    try:
        with open(file_path, "r") as f:
            return [u.strip() for u in f if u.strip()]
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return []


def run_parallel(urls, threads):
    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_url = {
            executor.submit(check_headers, url): url for url in urls
        }

        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                results.append(result)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="VulnScope - HTTP Security Header Analyzer"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="Scan a single URL")
    group.add_argument("--file", help="Scan multiple URLs from file")

    parser.add_argument("--threads", type=int, default=5,
                        help="Number of concurrent scans (default: 5)")

    parser.add_argument("--output", default="report.json",
                        help="Output JSON file name")

    args = parser.parse_args()

    # Load URLs
    if args.url:
        urls = [args.url.strip()]
    else:
        urls = load_urls(args.file)

    if not urls:
        print("[!] No valid URLs to scan")
        return

    # Normalize URLs
    urls = [
        u if u.startswith(("http://", "https://")) else "http://" + u
        for u in urls
    ]

    print("=" * 60)
    print("VulnScope - Advanced Security Scanner")
    print("=" * 60)

    # Run scans
    results = run_parallel(urls, args.threads)

    # Save report
    try:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)

        print(f"\n[+] Report saved as: {args.output}")

    except Exception as e:
        print(f"[ERROR] Failed to save report: {e}")


if __name__ == "__main__":
    main()
