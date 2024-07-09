import sys
import os
import filetype  # Use filetype package instead of magic
sys.path.append("lib")
from lib import *
from util import *

OUTPUT_DIR = "output"

def print_help():
    help_text = f"""Zeta Metadata Extractor - Extract metadata from various files
Usage:
    python cli.py <file>
Note:
    Results will be available in ./{OUTPUT_DIR}
Options:
    -h, --help        Show this help message and exit
"""
    print(help_text)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print_help()
        return

    file = sys.argv[1]
    kind = filetype.guess(file)
    if kind is None:
        print("Cannot guess file type!")
        return

    file_type = kind.mime
    print("File Type:", file_type)
    metadata = extract_metadata_file(file, file_type)

    print_data(metadata)

    # Append meta-metadata
    metadata = add_meta_metadata(metadata, file)

    create_result_folder()
    write_pdf(file, metadata)

if __name__ == "__main__":
    main()
