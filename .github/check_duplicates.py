import sys
import xml.etree.ElementTree as ET
from collections import defaultdict


def check_duplicates(file_paths):
    for path in file_paths:
        tree = ET.parse(path)
        root = tree.getroot()
        books = root.findall('.//Book')

        seen = defaultdict(int)

        for book in books:
            key = (book.get('Series'), book.get('Number'), book.get('Volume'), book.get('Year'))
            seen[key] += 1

        duplicates = {k: v for k, v in seen.items() if v > 1}

        if duplicates:
            print("Duplicates found:")
            for k, v in duplicates.items():
                print(f"Series: {k[0]}, Number: {k[1]}, Volume: {k[2]}, Year: {k[3]}, Count: {v}")
            sys.exit(1)
        else:
            print("No duplicates found.")
            sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_duplicates.py <path_to_xml_file>")
        sys.exit(1)

    files = sys.argv[1]
    print(f'Files: {files}')
    check_duplicates(files)
