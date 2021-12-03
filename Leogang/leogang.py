import pandas as pd
import os
import re

def main():
    path = 'C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\Leogang\\Bitrix exports'
    files = os.listdir(path)
    files_xls = [f for f in files if f[-4:] == 'xlsx']
    if 'tov pred.xlsx' in files_xls:
        files_xls.remove('tov pred.xlsx')
    if 'output.xlsx' in files_xls:
        files_xls.remove('output.xlsx')

    df = pd.DataFrame()
    for f in files_xls:
        data = pd.read_excel(os.path.join(path, f), engine='openpyxl')
        df = df.append(data)
        # for col in df.columns:
        #     print(col)

    # товарные предложения в отдельный датафрейм
    df2 = pd.read_excel(os.path.join(path, 'tov pred.xlsx'), engine='openpyxl')

    # #  FORMAT 9212 (2020) [866] > FORMAT 9212 (2020)
    # df2['Элемент каталога'] = df2['Элемент каталога'].str.replace(r'\s\[\S*\]', '')
    
    # # JOIN
    # df = df.rename({'Название': 'Элемент каталога'}, axis=1)
    # df2.merge(df, on='Элемент каталога', how='left')
    # df2.to_excel(os.path.join(path, "output.xlsx"))

    



if __name__ == '__main__':
    main()