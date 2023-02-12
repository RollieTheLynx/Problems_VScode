import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch(page):
    result = requests.get(page)
    # print(result.status_code)
    # print(result.headers)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    return soup


def get_projects(page):
    soup = fetch(page)
    table = soup.find("div", class_="property-box-archive type-row")
    items = table.find_all("h3", class_="entry-title")
    links = [item.find('a')['href'] for item in items]
    try:
        next_link = soup.find('a', class_='next page-numbers')['href']
        print(next_link)
    except TypeError:
        next_link = None
    return links, next_link


def parse_project(link):
    soup = fetch(link)
    name = soup.find('h1', class_='entry-title property-title').text
    description = soup.find(id='property-section-description').text
    price = soup.find('div', class_='text-right price').text
    params_li = soup.find(id='property-section-detail').find_all('li')
    image = soup.find('img', class_="attachment-homesweet-gallery-v2 size-homesweet-gallery-v2")['src']
    params = {}
    for param_li in params_li:
        param_name = param_li.find('span').text
        param_value = param_li.find('span').parent.text.split(': ')[-1]
        params[param_name] = param_value
    return name, description, price, image, params


def addToDf(link):
    def get_new_data(link, new_data):
        project_links, next_page = get_projects(link)
        for link in project_links:
            new_line = parse_project(link)
            new_data.append(new_line)
        if next_page is not None:
            new_data = get_new_data(next_page, new_data)
        return new_data

    data = []
    data = get_new_data(link, data)
    df = pd.DataFrame(data, columns=['name', 'description', 'price', 'image', 'params'])
    df_params = pd.json_normalize(df['params'])  # dict params в отдельные колонки
    df = pd.concat([df, df_params], axis=1)
    df = df.drop(columns=['params'])
    return df


sale = 'https://terigroup.ru/properties/?filter-contract=SALE'
ongoing_df = addToDf(sale)
print(ongoing_df)

path = 'teri group.xlsx'
with pd.ExcelWriter(path) as writer:
    ongoing_df.to_excel(writer, sheet_name='Ongoing', index=False)
