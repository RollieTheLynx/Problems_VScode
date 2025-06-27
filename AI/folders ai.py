# -*- coding: utf-8 -*-
"""
This was written with Deepseek!
"""

import os

def list_files_with_extensions(path):
    try:
        for root, dirs, files in os.walk(path):
            print(f"Searching directory: {root}")
            for file in files:
                filename, extension = os.path.splitext(file)
                print(f"File: {filename} | Extension: {extension}")
        return True
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return False

# Example usage
if __name__ == "__main__":
    list_files_with_extensions("E:\Torrents\The Coppersmith's Bride (Digital)")
