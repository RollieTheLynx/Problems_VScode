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
    
    for aline in range(1,len(lines)):
        aline = lines[aline].find_all("span")
        for column in range(0,len(aline)):
            database_entry = []
            database_entry.append(aline[0].find("a")["href"][1:]) #eng name
            database_entry.append(aline[0].get_text()) # rus name
            database_entry.append(aline[1].get_text()) # pokedex
            database_entry.append('https://pokemonov.net/' + aline[2].find("img")["src"][1:]) #img link
            types = ""
            for typ in aline[3].find_all("a"):
                types = types + typ.get_text() + " "
            database_entry.append(types) # type
        database.append(database_entry)
    button = soup.find("a", {"title":"Следующая страница"})
    return button, data

#%%
start_page = "https://pokemonov.net/pokedex/"
new_link = start_page
database = [['Англ имя', 'Рус имя', 'Pokedex', 'Изображение', 'Тип']]

while True:
    button, new_database = parse(new_link, database)
    try:
        new_link = start_page + button['href'][9:]
    except:
        break
    else:
        database = new_database
        sleep(randrange(3,9))

#%%   
df = pandas.DataFrame.from_records(database)
df.columns = database[0] # делаем первую строку заголовком пандас
df = df.drop([0]) # и удаляем ее из тела таблицы
df['Англ имя'] = df['Англ имя'].str.capitalize() 
df.to_excel("pokedex.xlsx", index=False)
