# 📦 Project File Collector

A lightweight Python command-line utility that recursively scans a project directory, reads all supported files, and concatenates their contents into a single output file while preserving file paths as headers.

This tool is particularly useful for:

* Feeding entire projects into LLMs (ChatGPT, Claude, Gemini, etc.)
* Code review and auditing
* Project archiving
* Documentation generation
* Creating portable project snapshots

---

# 🚀 Features

✅ Recursive directory traversal

✅ Automatic file path headers

✅ Configurable text encoding

✅ Ignore binary and media files

✅ Custom ignore extension support

✅ Single-file export of an entire project

✅ Cross-platform (Windows, Linux, macOS)

---

# 🎯 Problem It Solves

When working with AI assistants, code reviews, or documentation tools, sharing an entire project structure can be difficult.

This utility solves that problem by:

1. Traversing all files recursively.
2. Ignoring unwanted binary/media files.
3. Adding file path metadata before each file.
4. Merging everything into one readable text document.

The generated file can then be directly uploaded to AI systems or shared with collaborators.

---

# 🛠 Prerequisites

* Python 3.9+
* Read access to the target directory
* Sufficient disk space for the generated output file

Verify your Python installation:

```bash
python --version
```

---

Move into the project directory:

```bash
cd project-file-collector
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

No external dependencies are required.

---

# ⚡ Quick Start

Basic usage:

```bash
python collect_files.py ./my_project
```

Output:

```text
project_files_concat.txt
```

---

## Custom Output File

```bash
python collect_files.py ./my_project -o output.txt
```

---

## Specify Encoding

```bash
python collect_files.py ./my_project --encoding utf-8
```

---

## Ignore Additional Extensions

```bash
python collect_files.py ./my_project --ignore .log .csv .json
```

---

# 📖 Command Reference

```bash
python collect_files.py SOURCE_DIR [OPTIONS]
```

### Arguments

| Argument   | Description            |
| ---------- | ---------------------- |
| source_dir | Root directory to scan |

### Options

| Option       | Description                     |
| ------------ | ------------------------------- |
| -o, --output | Output filename                 |
| --encoding   | File encoding                   |
| --ignore     | Additional extensions to ignore |

---

# 🔍 Example

Directory:

```text
sample_project/
├── app.py
├── config.py
└── utils/
    └── helper.py
```

Command:

```bash
python collect_files.py sample_project
```

Generated output:

```text
===== File: app.py =====

print("Hello World")

===== File: config.py =====

DEBUG = True

===== File: utils/helper.py =====

def helper():
    pass
```

---

# 📂 Project Structure

```text
project-file-collector/
│
├── collect_files.py
├── README.md
└── project_files_concat.txt
```

### File Descriptions

| File                     | Purpose                      |
| ------------------------ | ---------------------------- |
| collect_files.py         | Main application entry point |
| README.md                | Project documentation        |
| project_files_concat.txt | Generated output file        |

---

# ⚙️ Configuration

The project currently does not require a `.env` file.

Configuration is handled through command-line arguments:

```bash
--output
--encoding
--ignore
```

---

# 🧠 Processing Pipeline

The application follows the following workflow:

```text
User Input
     │
     ▼
Validate Source Directory
     │
     ▼
Recursive File Discovery
     │
     ▼
Extension Filtering
     │
     ▼
Read File Content
     │
     ▼
Generate Path Header
     │
     ▼
Append Content
     │
     ▼
Write To Output File
     │
     ▼
Finished
```

---

# 🚫 Default Ignored File Types

The following file extensions are ignored by default:

```text
.pyc
.pyo
.so
.dll
.exe

.jpg
.jpeg
.png
.gif
.bmp

.mp3
.mp4
.avi
.mov

.zip
.tar
.gz
.rar
.7z
```

These files are skipped to prevent binary data corruption and reduce output size.

---

# ⚠️ Error Handling

The application includes protection against:

* Invalid directories
* File read failures
* Encoding issues
* Permission errors

If a file cannot be read, the generated output contains:

```text
[Error reading file: ...]
```

instead of terminating the entire process.

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

---

# 🧪 Future Improvements

Potential enhancements:

* Multithreaded file reading
* Progress bar support
* Include/Exclude path patterns
* JSON export
* Markdown export
* Directory statistics
* GUI version
* Compression support

---

# 🏗 Built With

* Python 3
* pathlib
* argparse
* os
* sys

---

# 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# 👨‍💻 Author

Developed for efficient project aggregation, code review, AI-assisted analysis, and documentation workflows.
