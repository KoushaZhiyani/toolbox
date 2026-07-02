import argparse
from datetime import date
from sqlalchemy import create_engine, inspect, text


def build_connection_url(args):
    if args.db_type == "duckdb":
        return f"duckdb:///{args.database}"

    if args.db_type == "sqlite":
        return f"sqlite:///{args.database}"

    if args.db_type == "postgres":
        return (
            f"postgresql+psycopg2://{args.user}:{args.password}"
            f"@{args.host}:{args.port}/{args.database}"
        )

    if args.db_type == "mysql":
        return (
            f"mysql+pymysql://{args.user}:{args.password}"
            f"@{args.host}:{args.port}/{args.database}"
        )

    if args.db_type == "sqlserver":
        return (
            f"mssql+pyodbc://{args.user}:{args.password}"
            f"@{args.host}:{args.port}/{args.database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )

    raise ValueError(f"Unsupported database type: {args.db_type}")


def is_datetime_column(column_type):
    column_type = str(column_type).lower()

    return any(
        item in column_type
        for item in [
            "date",
            "time",
            "datetime",
            "timestamp",
        ]
    )


def get_tables(engine):
    inspector = inspect(engine)
    return inspector.get_table_names()


def get_datetime_columns(engine, table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)

    return [
        column["name"]
        for column in columns
        if is_datetime_column(column["type"])
    ]


def choose_item(items, title):
    print(f"\n{title}")

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:
        choice = input("\nEnter number or name: ").strip()

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(items):
                return items[index]

        if choice in items:
            return choice

        print("Invalid choice.")


def count_rows(engine, table_name, date_column, target_date):
    query = text(f"""
        SELECT COUNT(*)
        FROM {table_name}
        WHERE CAST({date_column} AS DATE) = :target_date
    """)

    with engine.connect() as conn:
        return conn.execute(query, {"target_date": target_date}).scalar()


def delete_rows(engine, table_name, date_column, target_date):
    query = text(f"""
        DELETE FROM {table_name}
        WHERE CAST({date_column} AS DATE) = :target_date
    """)

    with engine.begin() as conn:
        conn.execute(query, {"target_date": target_date})


def main():
    parser = argparse.ArgumentParser(
        description="Delete rows from different databases by date."
    )

    parser.add_argument(
        "--db-type",
        required=True,
        choices=["duckdb", "sqlite", "postgres", "mysql", "sqlserver"],
    )

    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=None)
    parser.add_argument("--user")
    parser.add_argument("--password")
    parser.add_argument("--database", required=True)

    parser.add_argument("--table")
    parser.add_argument("--all-tables", action="store_true")

    parser.add_argument("--date-column")
    parser.add_argument("--target-date", default=date.today().isoformat())

    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--yes", action="store_true")

    args = parser.parse_args()

    if args.db_type == "postgres" and args.port is None:
        args.port = 5432

    if args.db_type == "mysql" and args.port is None:
        args.port = 3306

    if args.db_type == "sqlserver" and args.port is None:
        args.port = 1433

    target_date = date.fromisoformat(args.target_date)

    connection_url = build_connection_url(args)
    engine = create_engine(connection_url)

    tables = get_tables(engine)

    if not tables:
        print("No tables found.")
        return

    if args.all_tables:
        selected_tables = tables
    elif args.table:
        if args.table not in tables:
            print(f"Table '{args.table}' not found.")
            print("Available tables:")
            for table in tables:
                print(f"- {table}")
            return

        selected_tables = [args.table]
    else:
        selected_tables = [choose_item(tables, "Select table")]

    for table in selected_tables:
        datetime_columns = get_datetime_columns(engine, table)

        if not datetime_columns:
            print(f"SKIP: {table} | No date/time column found.")
            continue

        if args.date_column:
            if args.date_column not in datetime_columns:
                print(f"SKIP: {table} | Invalid date column: {args.date_column}")
                continue

            selected_column = args.date_column
        elif len(datetime_columns) == 1:
            selected_column = datetime_columns[0]
        else:
            selected_column = choose_item(
                datetime_columns,
                f"Select date column for table '{table}'"
            )

        rows_count = count_rows(
            engine=engine,
            table_name=table,
            date_column=selected_column,
            target_date=target_date,
        )

        print(
            f"\nTable: {table} | "
            f"Date column: {selected_column} | "
            f"Date: {target_date} | "
            f"Rows: {rows_count}"
        )

        if rows_count == 0:
            continue

        if not args.execute:
            print("DRY RUN: Nothing deleted. Use --execute to delete.")
            continue

        if not args.yes:
            confirm = input(f"Delete {rows_count} rows from {table}? Type yes: ")
            if confirm.lower().strip() != "yes":
                print("Cancelled.")
                continue

        delete_rows(
            engine=engine,
            table_name=table,
            date_column=selected_column,
            target_date=target_date,
        )

        print(f"Deleted {rows_count} rows from {table}.")


if __name__ == "__main__":
    main()