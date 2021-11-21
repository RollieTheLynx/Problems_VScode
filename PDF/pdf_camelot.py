# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:00 2020

@author: Rollie
"""

'''
Camelot - не видит Ghostscript
'''

# import camelot
# tables = camelot.read_pdf('foo.pdf')
# tables
# tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
# tables[0]
# <Table shape=(7, 7)>
# tables[0].parsing_report
# {
#     'accuracy': 99.02,
#     'whitespace': 12.24,
#     'order': 1,
#     'page': 1
# }
# tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
# tables[0].df # get a pandas DataFrame!

# import PyPDF2
# pdfFileObj = open('C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\foo.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj)
# print(pageObj.extractText())

'''
Tabula - только таблицы
'''

# import tabula
# file1 = "C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\data1.pdf"
# table = tabula.read_pdf(file1,pages=1)
# print(table[0])

# file2 = "C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\data2.pdf"
# # To read table in first page of PDF file
# table1 = tabula.read_pdf(file2 ,pages=1)
# # To read tables in secord page of PDF file
# table2 = tabula.read_pdf(file2 ,pages=2)
# print(table1[0])
# print(table2[0])

# # To read multiple tables we need to add extra parameter
# # multiple_tables = True -> Read multiple tables as independent tables
# # multiple_tables = False -> Read multiple tables as single table
# file3 = "C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\data3.pdf"
# tables = tabula.read_pdf(file3 ,pages=1, multiple_tables=True)
# print(tables[0])
# print(tables[1])
# tables = tabula.read_pdf(file3 ,pages=1,multiple_tables=False)
# tables[0]

# # Converting tables in 1 page of PDF file to CSV
# # output just the first page tables in the PDF to a CSV
# tabula.convert_into(file3, "Name_of_csv_file.csv")
# # Converting all table in PDF file to CSV
# tabula.convert_into(file3,"Name_of_csv_file2.csv",all = True)

# file = 'C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\PDF\\foo.pdf'
# table = tabula.read_pdf(file,pages=1)
# print(table[0])

'''
spacy
'''

import spacy
nlp = spacy.load('en_core_web_sm')

# Process whole documents
text = "Google was initially funded by an August 1998 contribution of $100,000 from Andy Bechtolsheim, co-founder of Sun Microsystems; the money was given before Google was incorporated.[30] Google received money from three other angel investors in 1998: Amazon.com founder Jeff Bezos, Stanford University computer science professor David Cheriton, and entrepreneur Ram Shriram.[31] Between these initial investors, friends, and family Google raised around 1 million dollars, which is what allowed them to open up their original shop in Menlo Park, California"
doc = nlp(text)

# for token in doc:
#     print(token)

## only nouns
# for token in doc:
#     if token.pos_ == "NOUN":
#         print(token)

# Named Entity Recognition
for entity in doc.ents:
        print(entity.text, entity.label_)
