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
3. Setup Virtual envoirment Linux :
    ```sh
    cd metaextractor-zeta
    python -m venv .
    . bin/activate
    ```

4. Setup Virtual envoirment windows:
    ```sh
   cd metaextractor-zeta
    python -m venv .
find and run ```
metaextractor-zeta-main\Scripts\activate.bat ```

or type in powershell

    Scripts\activate.bat

## Here's a step-by-step guide to adding FFmpeg to the system PATH on Windows for mp4 meta data extraction:

### Step-by-Step Guide For Windows

1. **Download and Extract FFmpeg**:
   - Go to [FFmpeg's official website](https://ffmpeg.org/download.html).
   - Download the build suitable for your system (Windows).
   - Extract the downloaded ZIP file to a directory of your choice. For example, `C:\ffmpeg`.

2. **Locate the `bin` Folder**:
   - After extracting, navigate to the folder where FFmpeg was extracted. You should see a folder named `bin` inside the FFmpeg directory. For example, `C:\ffmpeg\bin`.

3. **Add the `bin` Folder to System PATH**:

   1. **Open Environment Variables**:
      - Press `Win + S` (or open the Start Menu) and type "env".
      - Select "Edit the system environment variables" from the search results.

   2. **Open Environment Variables Window**:
      - In the System Properties window, click on the "Environment Variables..." button near the bottom right.

   3. **Edit the PATH Variable**:
      - In the Environment Variables window, you will see two sections: "User variables" and "System variables".
      - In the "System variables" section, scroll down and find the variable named `Path`.
      - Select `Path` and click on the "Edit..." button.

   4. **Add New PATH Entry**:
      - In the Edit Environment Variable window, click on the "New" button on the right side.
      - Enter the path to the `bin` folder inside the FFmpeg directory. For example, `C:\ffmpeg\bin`.

   5. **Save the Changes**:
      - Click OK to close the Edit Environment Variable window.
      - Click OK again to close the Environment Variables window.
      - Click OK to close the System Properties window.

### Verify the Configuration

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

2. **Check ffmpeg Installation**:
   - In the Command Prompt, type the following command and press Enter:
     ```bash
     ffprobe -version
     ```
   - If the PATH is set correctly, you should see the version information for `ffprobe`.

### Step-by-Step Guide For Linux 
## Here's a step-by-step guide to installing FFmpeg on Ubuntu and adding it to your system PATH:

### Step-by-Step Guide for Ubuntu

1. **Install FFmpeg**:

   - Open a terminal and run the following command to update the package list:
     ```bash
     sudo apt update
     ```

   - Install FFmpeg using the following command:
     ```bash
     sudo apt install ffmpeg
     ```

   - Confirm the installation by checking the version:
     ```bash
     ffmpeg -version
     ```

2. **Add FFmpeg to the System PATH**:

   On Ubuntu, FFmpeg is usually installed in a directory that is already in your system PATH. However, if for some reason it is not, you can manually add it to your PATH.

   - First, find out where FFmpeg is installed:
     ```bash
     which ffmpeg
     ```

   - This will output the path to the `ffmpeg` executable, typically `/usr/bin/ffmpeg`.

3. **Edit the `.bashrc` File**:

   - Open the `.bashrc` file in your home directory using a text editor. For example, with `nano`:
     ```bash
     nano ~/.bashrc
     ```

   - Add the following line at the end of the file, replacing `/usr/bin` with the actual directory if it is different:
     ```bash
     export PATH="$PATH:/usr/bin"
     ```

   - Save the file and exit the editor. In `nano`, you can do this by pressing `Ctrl + X`, then `Y`, and `Enter`.

4. **Apply the Changes**:

   - To apply the changes made to `.bashrc`, run the following command:
     ```bash
     source ~/.bashrc
     ```

5. **Verify the Configuration**:

   - Open a new terminal window and check the FFmpeg installation:
     ```bash
     ffmpeg -version
     ```

   - You should see the version information for FFmpeg, indicating that it is correctly installed and accessible.


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

### License

This project is licensed under the GPL License. See the LICENSE file for details.
