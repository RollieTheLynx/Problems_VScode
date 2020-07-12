import requests
from bs4 import BeautifulSoup
import pandas
from time import sleep
from random import randrange

#%%
def parse(link, data):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(link, headers = headers)
    #print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find(class_ = "info allmoves center")
    lines = table.find_all("li")
    database = data
    
    for aline in range(0,len(lines)):
        aline = lines[aline].find_all("span")
        database_entry = []
        for column in range(0,len(aline)):
            database_entry.append(aline[column].get_text())
        database.append(database_entry)
    button = soup.find("a", {"title":"Следующая страница"})
    return button, data

#%%
start_page = "https://pokemonov.net/pokedex/"
new_link = start_page
database = []

while True:
    button, new_database = parse(new_link, database)
    try:
        new_link = start_page + button['href'][9:]
        # if new_link == "https://pokemonov.net/pokedex/page/4":
        #     break
    except:
        break
    else:
        database = new_database
        sleep(randrange(3,15))

#%%   
df = pandas.DataFrame.from_records(database)
df.to_excel("pokedex.xlsx", index=False)
