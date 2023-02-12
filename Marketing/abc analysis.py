# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:40:54 2020

@author: Rollie
"""
import pandas as pd
import random
import string

data = []
for i in range(100):
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    revenue = round(random.uniform(-10, 100000), 2)
    data.append([name, revenue])

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Revenue'])
print(df.head())

df = df.sort_values(by=['Revenue'], ascending=False, ignore_index=True)
print(df.head())

sum = df['Revenue'].sum()
df['Share of total'] = df['Revenue']/sum
print(df.head())

df['Share accrued'] = df['Share of total'].cumsum()
print(df.head())

df.loc[df['Share accrued'] <= 0.8, 'ABC rank'] = 'A' 
df.loc[(df['Share accrued'] >0.8) & (df['Share accrued'] <=0.95), 'ABC rank'] = 'B'
df.loc[df['Share accrued'] >0.95, 'ABC rank'] = 'C'
print(df.head(100))

print('A: ' + str(df["ABC rank"].value_counts()[['A']].sum()))
print('B: ' + str(df["ABC rank"].value_counts()[['B']].sum()))
print('C: ' + str(df["ABC rank"].value_counts()[['C']].sum()))
