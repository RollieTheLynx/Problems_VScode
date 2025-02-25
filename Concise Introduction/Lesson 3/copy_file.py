# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:44:45 2020

@author: Rollie
"""


""" Opens two files and copies one into the other line by line. """
"""
Exercise: Convert this function to a standalone program or script that
takes two file names from the command line and copies one to the other.

Steps:
1. Delete "Def" line. You don't need it.
2. Use Edit menu of Spyder to Unindent all the lines.
3. import the system library sys
4. sys.argv is a list of the filenames following the program name.
   sys.argv[0] is the program name, sys.argv[1] is first argument, etc.
   Get the infilename and outfilename from this list.
5. Save the program
6. Run the program from a terminal window (Mac) a cmd.exe window (PC) or
   a command prompt within Spyder (use Tools>Open command prompt)

Here is how running it should look:
>python copy_file.py humptydumpty.txt newhumpty.txt
"""
    
import sys
infilename = sys.argv[1]
outfilename = sys.argv[2]
infile = open(infilename)
outfile = open(outfilename,'w')

for line in infile:
    outfile.write(line)
    
infile.close()
outfile.close()