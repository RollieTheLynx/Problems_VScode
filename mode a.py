# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:38:16 2020

@author: Rollie
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randrange

df = pd.DataFrame([['a', 'b'], ['c', 'd']],

                   index=['row 1', 'row 2'],

                   columns=['col 1', 'col 2'])


with pd.ExcelWriter('output.xlsx', engine='openpyxl', mode='a') as writer:  

    df.to_excel(writer, sheet_name='Sheet_name_3')