from bs4 import BeautifulSoup
import os

folder = 'C:\\Users\\Mike\\Desktop\\ефыл'
ad_list = []
output = []

for file in os.listdir(folder):
    if file.endswith(".html"):
        page = os.path.join(folder, file)
        #print(page)
        with open(page, encoding="utf8") as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            for ad in soup.find_all('div', {'class' : 'title'}):
                if "№" in ad.get_text():
                    ad_list.append(ad.get_text())

for item in ad_list:
    number = int(item.split("№")[1])
    if number not in output:
        output.append(number)

with open('C:\\Users\\Mike\\Desktop\\Startkey Vizyon Gayrim.txt', 'w', encoding='utf8') as f:
    for line in output:
        f.write(f"{line}\n")

