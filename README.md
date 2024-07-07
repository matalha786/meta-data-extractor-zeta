## Zeta Data Extractor

Zeta Data Extractor is a tool designed to gather hidden information from documents and images, providing insights into the target by extracting metadata. This tool supports various file types and extracts comprehensive metadata attributes and meta-metadata attributes.

### Features

- **Supports Various File Types**: Extract metadata from PDFs, DOCX files, images (JPEG, PNG), and more.
- **Extract Comprehensive Metadata**: Gather details such as the document's author, creation and modification dates, software used, and geolocation (for images).
- **Meta-Metadata Extraction**: Extracts metadata about the metadata itself for enhanced analysis.

### Requirements

- Python 3.x
- `pypdf`
- `ffmpeg`
- `PIL`
- `python-docx`
- `openpyxl`
- `python-pptx`
- `fpdf`
- `python-magic`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Zeta-osint/metaextractor-zeta.git
    cd metaextractor-zeta
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

```sh
python cli.py [options] <file>
```

#### Options

- `-h, --help`: Show help message and exit

### Example

To extract metadata from a PDF file:

```sh
python cli.py example.pdf
```

### Output

The extracted metadata will be saved in a structured format in a PDF file within the `result` folder. If a file with the same name already exists, a counter will be appended to the filename to avoid overwriting.

