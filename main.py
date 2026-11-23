import os

PARTS = [
    "I did not miss that spot. ",
    "My sensors classified it as a protected dust-bunny habitat, ",
    "and disturbing native wildlife would void my warranty.",
]


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
