import pandas
import requests
from bs4 import BeautifulSoup

start_page = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(start_page, headers = headers)
soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all('table')
writer = pandas.ExcelWriter('pokedex_bulbagarden.xlsx', engine='xlsxwriter')
generation_counter = 0

for table in tables[1:9]:
    generation_counter += 1
    rows = table.find_all('tr')
    heads = [el.get_text().strip() for el in rows[0].find_all('th')]
    rows_list = []

    for row in rows[1:]:
        cell = row.find_all('td')
        dict1 = {heads[0]: cell[0].get_text().strip(),
                 heads[1]: cell[1].get_text().strip(),
                 heads[3]: cell[2].get_text().strip(),
                 heads[4]: ', '.join([el.get_text().strip() for el in cell[3:]]),
                 'link': 'https://bulbapedia.bulbagarden.net' + row.find('a')['href'],
                 'image': 'https:' + row.find('img')['src']}
        rows_list.append(dict1)

    df = pandas.DataFrame(rows_list)
    df.to_excel(writer, index=False, sheet_name=f' Generation {generation_counter}')

writer.save()

