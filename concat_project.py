import os
import sys
import argparse
from pathlib import Path

def collect_files(root_dir, output_file, encoding='utf-8', ignore_extensions=None):
    """
    Recursively reads all files in root_dir and saves them to output_file
    with a path header.
    """
    if ignore_extensions is None:
        ignore_extensions = ['.pyc', '.pyo', '.so', '.dll', '.exe',
                             '.jpg', '.jpeg', '.png', '.gif', '.bmp',
                             '.mp3', '.mp4', '.avi', '.mov',
                             '.zip', '.tar', '.gz', '.rar', '.7z']

    root_path = Path(root_dir)
    if not root_path.is_dir():
        raise NotADirectoryError(f"'{root_dir}' is not a valid directory")

    with open(output_file, 'w', encoding=encoding) as out_f:
        for file_path in root_path.rglob('*'):
            # Process only regular files (not directories)
            if not file_path.is_file():
                continue

            # Skip if the file extension is in the ignore list
            if file_path.suffix.lower() in ignore_extensions:
                continue

            # Write header with relative and full path
            relative_path = file_path.relative_to(root_path)
            out_f.write(f"===== File: {relative_path} (full: {file_path.resolve()}) =====\n")

            # Read and write file content
            try:
                with open(file_path, 'r', encoding=encoding) as in_f:
                    content = in_f.read()
                    out_f.write(content)
                    # Add a newline at the end if needed
                    if content and not content.endswith('\n'):
                        out_f.write('\n')
            except Exception as e:
                out_f.write(f"[Error reading file: {e}]\n")

            # Separator between files
            out_f.write("\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursively collects all files of a project with a path header into a single file."
    )
    parser.add_argument("source_dir", help="Root directory of the project")
    parser.add_argument("-o", "--output", default="project_files_concat.txt",
                        help="Output file name (default: project_files_concat.txt)")
    parser.add_argument("--encoding", default="utf-8",
                        help="Encoding for reading/writing (default: utf-8)")
    parser.add_argument("--ignore", nargs="*",
                        help="List of extensions to ignore (e.g., .pyc .jpg) - if not specified, the default list is used")

    args = parser.parse_args()

    # Determine the ignore list
    if args.ignore is not None:
        ignore_list = [ext if ext.startswith('.') else f'.{ext}' for ext in args.ignore]
    else:
        ignore_list = ['.pyc', '.pyo', '.so', '.dll', '.exe',
                       '.jpg', '.jpeg', '.png', '.gif', '.bmp',
                       '.mp3', '.mp4', '.avi', '.mov',
                       '.zip', '.tar', '.gz', '.rar', '.7z']

    try:
        collect_files(args.source_dir, args.output, encoding=args.encoding, ignore_extensions=ignore_list)
        print(f"Operation successful. Output saved to '{args.output}'.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
