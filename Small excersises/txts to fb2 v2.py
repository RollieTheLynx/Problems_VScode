import os
import html
import string
from datetime import datetime
from collections import defaultdict

MAX_SIZE = 100 * 1024 * 1024  # 100 MB


def read_txt_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return html.unescape(content)


def get_group_key(title):
    title = title.strip()
    if not title:
        return "#"
    first = title[0].upper()
    return first if first in string.ascii_uppercase else "#"


def build_grouped_body(content_blocks):
    grouped = defaultdict(list)

    for title, text in content_blocks:
        key = get_group_key(title)
        grouped[key].append((title, text))

    body = ""

    for letter in sorted(grouped.keys()):
        body += f"""
        <section>
            <title><p>{letter}</p></title>
        """

        for title, text in grouped[letter]:
            body += f"""
            <section>
                <title><p>{title}</p></title>
                <p>{text}</p>
            </section>
            """

        body += "\n</section>"

    return body


def wrap_fb2(content_blocks, book_title, part_number):
    date_str = datetime.now().strftime("%Y-%m-%d")
    body = build_grouped_body(content_blocks)

    return f"""<?xml version="1.0" encoding="utf-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0">
    <description>
        <title-info>
            <book-title>{book_title} (Part {part_number})</book-title>
            <lang>en</lang>
        </title-info>
        <document-info>
            <date value="{date_str}">{date_str}</date>
        </document-info>
    </description>
    <body>
        {body}
    </body>
</FictionBook>
"""


def split_into_books(folder_path, output_dir):
    folder_name = os.path.basename(folder_path.rstrip("/\\"))
    txt_files = sorted(
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".txt")
    )

    current_blocks = []
    current_size = 0
    part_number = 1

    os.makedirs(output_dir, exist_ok=True)

    for filename in txt_files:
        path = os.path.join(folder_path, filename)
        text = read_txt_file(path)
        title = os.path.splitext(filename)[0]

        estimated_size = len(text.encode("utf-8"))

        # If adding this file exceeds max size → flush current part
        if current_blocks and current_size + estimated_size > MAX_SIZE:
            fb2_content = wrap_fb2(current_blocks, folder_name, part_number)

            output_path = os.path.join(
                output_dir,
                f"{folder_name}_part{part_number}.fb2"
            )

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(fb2_content)

            part_number += 1
            current_blocks = []
            current_size = 0

        current_blocks.append((title, text))
        current_size += estimated_size

    # Write remaining content
    if current_blocks:
        fb2_content = wrap_fb2(current_blocks, folder_name, part_number)

        output_path = os.path.join(
            output_dir,
            f"{folder_name}_part{part_number}.fb2"
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(fb2_content)


if __name__ == "__main__":
    folders = [
        r"D:\\stories\\Literotica incest",
        r"D:\\stories\\Stulchik incest",
        r"D:\\stories\\Stulchik young",
        r"D:\\stories\\Stulchik zoo"
    ]

    output_base = r"C:\books\output"

    for folder in folders:
        split_into_books(folder, output_base)