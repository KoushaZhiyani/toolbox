# SQLite Database Preview Tool

A lightweight Python CLI utility that connects to a SQLite database, extracts table structures, and exports a preview of the first records from each table into a readable text file.

## Features

* Connects to any SQLite database file (`.db`, `.sqlite`, `.sqlite3`)
* Automatically detects all user-created tables
* Ignores SQLite system tables
* Displays column names for each table
* Extracts and logs the first 10 rows from every table
* Supports UTF-8 output for international characters
* Appends results to an existing output file instead of overwriting
* Adds execution timestamps for historical tracking

---

## Use Cases

This tool is useful for:

* Quickly inspecting unknown SQLite databases
* Database auditing and validation
* Sharing database samples with developers
* Creating lightweight database documentation
* Debugging ETL and migration processes

---

## Requirements

* Python 3.7+

No third-party dependencies are required.

---

## Usage

### Basic Usage

```bash
python sqlite_preview.py database.db
```

Output will be appended to:

```text
output.txt
```

### Custom Output File

```bash
python sqlite_preview.py database.db report.txt
```

---

## Example Output

```text
===== New run at 2026-06-19 14:35:21 =====
Database: sample.db

Table: Customers
==================================================

Id | Name | Email
-------------------------
1 | John Smith | john@example.com
2 | Sarah Lee | sarah@example.com

Table: Orders
==================================================

OrderId | CustomerId | Total
----------------------------
101 | 1 | 125.50
102 | 2 | 89.99
```

---

## Command-Line Arguments

| Argument         | Required | Description                  |
| ---------------- | -------- | ---------------------------- |
| sqlite_file_path | Yes      | Path to the SQLite database  |
| output_file_path | No       | Path to the output text file |

Example:

```bash
python sqlite_preview.py my_database.db results.txt
```

---

## How It Works

1. Opens a connection to the SQLite database.
2. Retrieves all non-system tables.
3. Reads table schema information.
4. Fetches up to 10 records from each table.
5. Writes formatted output to a text file.
6. Appends a timestamped execution header for every run.

---

## Error Handling

The tool gracefully handles:

* Missing command-line arguments
* Invalid database paths
* SQLite connection failures
* File write permission issues
* Empty databases
* Empty tables

---

## Example Workflow

```bash
python sqlite_preview.py production.db database_snapshot.txt
```

Result:

```text
database_snapshot.txt
```

will contain a structured snapshot of all tables and sample records for future reference.

---

## Project Structure

```text
.
├── sqlite_preview.py
├── output.txt
└── README.md
```

---

## License

MIT License

Feel free to use, modify, and distribute this project.
