from scanner.headers import check_headers

def main():
    print("=" * 50)
    print("        VulnScope - Security Scanner")
    print("=" * 50)

    while True:
        url = input("\nEnter target URL (or 'exit' to quit): ").strip()

        if url.lower() == "exit":
            print("\nExiting VulnScope...")
            break

        if not url.startswith("http"):
            url = "http://" + url

        check_headers(url)


if __name__ == "__main__":
    main()
