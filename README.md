# 🧰 Toolbox

A collection of practical Python utilities and command-line tools designed to simplify common development, data processing, and project maintenance tasks.

Each tool is self-contained and includes its own documentation, usage examples, and requirements.

---

## 🎯 Purpose

This repository serves as a personal toolbox of reusable scripts and utilities that solve real-world problems encountered during software development, database analysis, automation, and documentation workflows.

The goal is to keep useful tools organized in a single place while maintaining separate documentation for each utility.

---

## 📦 Available Tools

### 📂 Project File Collector

A command-line utility that recursively scans a project directory and combines the contents of supported files into a single structured text document.

**Use cases:**

* AI-assisted code analysis
* Code reviews
* Documentation generation
* Project archiving
* Source code sharing

**Key Features**

* Recursive directory traversal
* Automatic file path headers
* Binary file filtering
* Custom ignore rules
* Single-file export

📖 See: `Project_File_Collector/README.md`

---

### 🗄 SQLite Database Preview Tool

A lightweight utility for inspecting SQLite databases and exporting table structures along with sample records into a readable text report.

**Use cases:**

* Database auditing
* Data validation
* Migration verification
* Documentation generation
* Quick database inspection

**Key Features**

* Automatic table discovery
* Schema extraction
* Sample data preview
* UTF-8 support
* Timestamped reporting

📖 See: `SQLite_Database_Preview/README.md`

---
### 🧹 SQL Insert Cleaner

A lightweight utility for cleaning and transforming SQL `INSERT INTO` statements by removing unwanted columns and optionally renaming destination tables.

**Use cases:**

* Database migration
* ETL preprocessing
* Legacy system cleanup
* SQL dump transformation
* Schema refactoring

**Key Features**

* SQL INSERT parsing
* Flexible column exclusion rules
* Table renaming support
* Regex-based filtering
* SQL function preservation
* Clean output generation

📖 See: `SQL_Insert_Cleaner/README.md`

---

## 🚀 Why This Repository Exists

Over time, many small utilities are created to solve recurring development tasks. Storing them across multiple repositories can make discovery and maintenance difficult.

This repository provides a centralized location for:

* Reusable scripts
* Development utilities
* Database tools
* Automation helpers
* Documentation generators

---

### 🗑 Rows Delete by Date

A command-line utility for deleting rows from database tables based on a specified date using `DATE`, `DATETIME`, or `TIMESTAMP` columns.

Supports multiple database engines through SQLAlchemy and includes a safe dry-run mode to preview deletions before execution.

**Use cases:**

* Data cleanup
* Removing daily import records
* ETL reruns
* Test data reset
* Scheduled maintenance tasks

**Key Features**

* Multi-database support (DuckDB, SQLite, PostgreSQL, MySQL, SQL Server)
* Automatic table discovery
* Automatic date/time column detection
* Dry-run mode by default
* Interactive confirmation before deletion
* Single-table or all-table processing

📖 See: `Rows_Delete_by_Date/README.md`

---
## 📁 Repository Structure

```text
toolbox/
│
├── Project_File_Collector/
│   ├── README.md
│   └── ...
│
├── SQLite_Database_Preview/
│   ├── README.md
│   └── ...
│
├── SQL_Insert_Cleaner/
│   ├── README.md
│   └── ...
│
├── Rows_Delete_by_Date/
│   ├── README.md
│   └── ...
│
└── README.md
```
---

## 🛠 Requirements

Most tools are built with:

* Python 3.9+
* Standard Library only (whenever possible)

Individual requirements may vary and are documented inside each tool's directory.

---

## 📈 Future Additions

Planned categories include:

* File Processing Tools
* Database Utilities
* SQL Transformation Tools
* Data Cleaning Scripts
* Automation Helpers
* CLI Productivity Tools
* Documentation Generators

---

## 🤝 Contributions

Contributions, bug reports, and feature suggestions are welcome.

Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

---

## 📜 License

This repository is licensed under the MIT License.

See the LICENSE file for details.

---

## 👨‍💻 Author

Created and maintained by Kousha Zhiyani.

A growing collection of practical tools built to solve everyday engineering problems.