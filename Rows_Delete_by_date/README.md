# Delete Rows by Date

A command-line Python utility for deleting rows from different databases
based on a selected **DATE**, **DATETIME**, or **TIMESTAMP** column.

The tool supports multiple database engines through SQLAlchemy and can
be used safely in **dry-run mode** before applying any deletion.

------------------------------------------------------------------------

## Supported Databases

-   DuckDB
-   SQLite
-   PostgreSQL
-   MySQL
-   SQL Server

------------------------------------------------------------------------

## Features

-   Connect to multiple database engines using SQLAlchemy
-   Automatically list available tables
-   Detect `DATE`, `DATETIME`, and `TIMESTAMP` columns
-   Delete rows matching a specific date
-   Process a single table or all tables
-   Dry-run mode by default
-   Interactive confirmation before deletion
-   Optional non-interactive mode using `--yes`

------------------------------------------------------------------------

## Installation

Install the required packages:

``` bash
pip install sqlalchemy pandas
pip install duckdb duckdb-engine
pip install psycopg2-binary
pip install pymysql
pip install pyodbc
```

> **Note:** SQL Server requires the appropriate ODBC Driver to be
> installed.

------------------------------------------------------------------------

## Supported Database Types

  Database     `--db-type`
  ------------ -------------
  DuckDB       `duckdb`
  SQLite       `sqlite`
  PostgreSQL   `postgres`
  MySQL        `mysql`
  SQL Server   `sqlserver`

------------------------------------------------------------------------

## Usage

The script runs in **dry-run mode** by default.

``` bash
python delete_by_date.py --db-type duckdb --database "collector.duckdb"
```

Nothing is deleted unless `--execute` is specified.

------------------------------------------------------------------------

## Examples

### DuckDB

``` bash
python delete_by_date.py ^
  --db-type duckdb ^
  --database "C:\traffic-data-platform\storage\processed\collector.duckdb" ^
  --table collection_runs ^
  --date-column created_at ^
  --execute
```

### SQL Server

``` bash
python delete_by_date.py ^
  --db-type sqlserver ^
  --host localhost ^
  --user sa ^
  --password YOUR_PASSWORD ^
  --database TrafficDB ^
  --table collection_runs ^
  --date-column created_at ^
  --execute
```

### PostgreSQL

``` bash
python delete_by_date.py ^
  --db-type postgres ^
  --host localhost ^
  --user postgres ^
  --password YOUR_PASSWORD ^
  --database traffic_db ^
  --all-tables ^
  --execute
```

### MySQL

``` bash
python delete_by_date.py ^
  --db-type mysql ^
  --host localhost ^
  --user root ^
  --password YOUR_PASSWORD ^
  --database traffic_db ^
  --table collection_runs ^
  --execute
```

### SQLite

``` bash
python delete_by_date.py ^
  --db-type sqlite ^
  --database "traffic.sqlite" ^
  --table collection_runs ^
  --execute
```

------------------------------------------------------------------------

## Command-Line Arguments

  -----------------------------------------------------------------------
  Argument                       Description
  ------------------------------ ----------------------------------------
  `--db-type`                    Database engine (`duckdb`, `sqlite`,
                                 `postgres`, `mysql`, `sqlserver`)

  `--host`                       Database host

  `--port`                       Database port

  `--user`                       Database username

  `--password`                   Database password

  `--database`                   Database name or file path

  `--table`                      Process a specific table

  `--all-tables`                 Process every table

  `--date-column`                Date/Time column to use

  `--target-date`                Target date (`YYYY-MM-DD`)

  `--execute`                    Execute the DELETE statement

  `--yes`                        Skip confirmation prompts
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Safety

-   Dry-run mode is enabled by default.
-   Rows are deleted **only** when `--execute` is provided.
-   The script displays the number of matching rows before deletion.
-   Confirmation is required unless `--yes` is used.

------------------------------------------------------------------------

## Common Issues

### DuckDB

If you receive:

``` text
sqlalchemy.exc.NoSuchModuleError:
Can't load plugin: sqlalchemy.dialects:duckdb
```

Install the DuckDB SQLAlchemy driver:

``` bash
pip install duckdb duckdb-engine
```

### SQL Server

Install Microsoft's ODBC Driver (for example, ODBC Driver 17 or later)
and update the connection string if necessary.

------------------------------------------------------------------------

## Recommended Workflow

1.  Run the script without `--execute`.
2.  Verify the detected table and row count.
3.  Execute the deletion using `--execute`.
4.  Use `--yes` for automated or scheduled jobs only.

------------------------------------------------------------------------

## License

This project is provided as-is and can be freely adapted to your own
workflows.
