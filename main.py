from scanner.headers import check_headers


def main():
    print("=" * 50)
    print("        VulnScope - Security Scanner")
    print("=" * 50)

    while True:
        url = input("\nEnter target URL (or 'exit' to quit): ").strip()

        # Exit condition
        if url.lower() == "exit":
            print("\nExiting VulnScope...")
            break

        # Validate empty input
        if not url:
            print("[!] Please enter a valid URL")
            continue

        # Auto-add scheme if missing
        if not url.startswith(("http://", "https://")):
            url = "http://" + url

        # Run scanner
        result = check_headers(url)

        # Handle result safely
        if result and isinstance(result, dict):
            print("\n--- Scan Summary ---")
            print(f"Target URL     : {result.get('url', url)}")
            print(f"Headers Present: {len(result.get('present', []))}")
            print(f"Headers Missing: {len(result.get('missing', []))}")
            print("-" * 30)
        else:
            print("[!] Failed to retrieve scan results")


if __name__ == "__main__":
    main()
