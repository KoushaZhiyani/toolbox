#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys
import datetime

def log_print(message, log_file=None):
    """Print message to console and optionally write it to a log file."""
    print(message)
    if log_file:
        log_file.write(message + "\n")
        log_file.flush()

def main():
    # Check command-line arguments (at least one argument for the database path)
    if len(sys.argv) < 2:
        print("Usage: python script.py <sqlite_file_path> [output_file_path]")
        print("If output path is not given, 'output.txt' will be used.")
        sys.exit(1)

    db_path = sys.argv[1]
    # Second argument (optional) is the output file path; default is "output.txt"
    output_path = sys.argv[2] if len(sys.argv) >= 3 else "output.txt"

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

    # Open the output file in append mode with UTF-8 encoding to support non-ASCII characters
    try:
        log_file = open(output_path, "a", encoding="utf-8")
    except IOError as e:
        print(f"Error opening output file: {e}")
        conn.close()
        sys.exit(1)

    # Write a separator line with the current date and time at the start of each run
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_print(f"\n===== New run at {now} =====", log_file)
    log_print(f"Database: {db_path}", log_file)

    # Retrieve the names of all user tables (excluding system tables)
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    tables = cursor.fetchall()

    if not tables:
        log_print("No tables found in the database.", log_file)
    else:
        # Process each table
        for (table_name,) in tables:
            log_print(f"\nTable: {table_name}", log_file)
            log_print("=" * 50, log_file)

            # Get column information for the current table
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            col_names = [col[1] for col in columns]

            # Retrieve the first 10 rows
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 10;")
            rows = cursor.fetchall()

            if not rows:
                log_print("(Table is empty)", log_file)
                continue

            # Print the header (column names)
            header = " | ".join(col_names)
            log_print(header, log_file)
            log_print("-" * len(header), log_file)

            # Print each row
            for row in rows:
                log_print(" | ".join(str(val) for val in row), log_file)

            if len(rows) < 10:
                log_print(f"(Total rows available: {len(rows)})", log_file)

    # Close connections
    conn.close()
    log_file.close()

    # Final console message
    print(f"\n✅ Output successfully appended to '{output_path}'.")
    print(f"   (Full path: {output_path})")

if __name__ == "__main__":
    main()
