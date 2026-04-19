from scanner.headers import check_headers

def main():
    try:
        with open("urls.txt", "r") as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()

            if url:
                print("\n" + "=" * 50)
                print(f"Scanning: {url}")
                print("=" * 50)

                check_headers(url)

    except FileNotFoundError:
        print("Error: urls.txt file not found")

if __name__ == "__main__":
    main()