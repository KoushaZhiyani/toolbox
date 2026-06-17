import os
import sys
import argparse
from pathlib import Path

def collect_files(root_dir, output_file, encoding='utf-8', ignore_extensions=None):
    """
    تمام فایل‌های موجود در root_dir (به‌صورت بازگشتی) را خوانده و با هدر مسیر،
    در output_file ذخیره می‌کند.
    """
    if ignore_extensions is None:
        ignore_extensions = ['.pyc', '.pyo', '.so', '.dll', '.exe',
                             '.jpg', '.jpeg', '.png', '.gif', '.bmp',
                             '.mp3', '.mp4', '.avi', '.mov',
                             '.zip', '.tar', '.gz', '.rar', '.7z']

    root_path = Path(root_dir)
    if not root_path.is_dir():
        raise NotADirectoryError(f"'{root_dir}'不是一个有效的目录")

    with open(output_file, 'w', encoding=encoding) as out_f:
        for file_path in root_path.rglob('*'):
            # فقط فایل‌های معمولی (نه پوشه) را پردازش کن
            if not file_path.is_file():
                continue

            # اگر پسوند فایل در لیست نادیده‌گرفته‌ها باشد، رد کن
            if file_path.suffix.lower() in ignore_extensions:
                continue

            # نوشتن هدر شامل مسیر نسبی و کامل
            relative_path = file_path.relative_to(root_path)
            out_f.write(f"===== File: {relative_path} (full: {file_path.resolve()}) =====\n")

            # خواندن محتوای فایل و نوشتن آن
            try:
                with open(file_path, 'r', encoding=encoding) as in_f:
                    content = in_f.read()
                    out_f.write(content)
                    # در صورت نیاز یک خط جدید در انتها اضافه کن
                    if content and not content.endswith('\n'):
                        out_f.write('\n')
            except Exception as e:
                out_f.write(f"[خطا در خواندن فایل: {e}]\n")

            # جداکننده بین فایل‌ها
            out_f.write("\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="همه فایل‌های یک پروژه را به‌صورت بازگشتی با هدر مسیر، در یک فایل جمع‌آوری می‌کند."
    )
    parser.add_argument("source_dir", help="پوشه ریشه پروژه")
    parser.add_argument("-o", "--output", default="project_files_concat.txt",
                        help="نام فایل خروجی (پیش‌فرض: project_files_concat.txt)")
    parser.add_argument("--encoding", default="utf-8",
                        help="کدگذاری برای خواندن/نوشتن (پیش‌فرض: utf-8)")
    parser.add_argument("--ignore", nargs="*",
                        help="لیست پسوندهای نادیده‌گرفته (مثلاً .pyc .jpg) - در صورت ذکر نشدن، لیست پیش‌فرض استفاده می‌شود")

    args = parser.parse_args()

    # تعیین لیست نادیده‌گرفته‌ها
    if args.ignore is not None:
        ignore_list = [ext if ext.startswith('.') else f'.{ext}' for ext in args.ignore]
    else:
        ignore_list = ['.pyc', '.pyo', '.so', '.dll', '.exe',
                       '.jpg', '.jpeg', '.png', '.gif', '.bmp',
                       '.mp3', '.mp4', '.avi', '.mov',
                       '.zip', '.tar', '.gz', '.rar', '.7z']

    try:
        collect_files(args.source_dir, args.output, encoding=args.encoding, ignore_extensions=ignore_list)
        print(f"عملیات با موفقیت انجام شد. خروجی در فایل '{args.output}' ذخیره گردید.")
    except Exception as e:
        print(f"خطا: {e}", file=sys.stderr)
        sys.exit(1)