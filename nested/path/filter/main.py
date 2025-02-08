from pathlib import Path

VERSION = "1.0.0"

def main():
    with Path("data/hello-release-filter/message.txt").open(
        "r", encoding="utf8"
    ) as f:
        message = f.read()
    with Path("BP/hello_release_filter.txt").open("w", encoding="utf8") as f:
        f.write(
            f"Version: {VERSION}\n"
            f"Message: {message.strip()}\n"
        )

if __name__ == '__main__':
    main()
