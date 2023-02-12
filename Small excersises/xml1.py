# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/xml.etree.elementtree.html#tutorial

"""
import xml.etree.ElementTree as ET
import pandas as pd

# data = '''<person>
# <name>Chuck</name>
# <phone type = "intl">
# +1 734 303 4456
# </phone>
# <email hide = "yes" />
# </person>'''

# tree = ET.fromstring(data)
# print("Name:", tree.find("name").text)
# print("Attr:", tree.find("email").get("hide"))

file = 'cd_catalog.xml'

tree = ET.parse(file)
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)


df = pd.read_xml(file)
print(df)
