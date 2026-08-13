import os
from get_proxies import get_proxies
from check_proxies import check_proxy

def main():
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    valid_proxies = []

    valid_proxies_path = os.path.join(output_dir, "valid_proxies.txt")
    if os.path.exists(valid_proxies_path):
        print("Checking if existing proxies are still valid...")
        still_valid = check_proxy(valid_proxies_path)
        print(f"Found {len(still_valid)} valid proxies from the existing list.")
        valid_proxies += still_valid

    print("Fetching new proxies...")
    new_proxies = get_proxies()
    new_proxies = list(set(new_proxies))
    print(f"Fetched {len(new_proxies)} new proxies.")

    proxies_path = os.path.join(output_dir, "proxies.txt")
    with open(proxies_path, "w") as f:
        for i in new_proxies:
            f.write(i + "\n")
    print("New proxies have been written to 'proxies.txt'.")

    print("Checking the validity of new proxies...")
    new_valid_proxies = check_proxy(proxies_path)
    print(f"Found {len(new_valid_proxies)} valid proxies from the new list.")
    valid_proxies += new_valid_proxies

    # Cleaning valid proxies
    cleaned_valid = []
    seen = set()

    for proxy in valid_proxies:
        proxy = proxy.strip()
        proxy = proxy.replace("http://", "").replace("https://", "")
        if proxy and proxy not in seen:
            seen.add(proxy)
            cleaned_valid.append(proxy)

    with open(valid_proxies_path, "w") as f:
        for p in cleaned_valid:
            f.write(p + "\n")
    print(f"Total valid proxies written to '{valid_proxies_path}': {len(cleaned_valid)}")


    preview_path = "valid_proxies_preview.txt"
    with open(preview_path, "w") as f:
        for p in cleaned_valid[-10:]:
            f.write(p + "\n")
    print(f"Preview 10 proxies written to '{preview_path}'.")

if __name__ == "__main__":
    main()
