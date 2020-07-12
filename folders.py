# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pathlib import Path

#list of file by pattern
path = Path()
for file in path.glob("*.py"):
    print(file)