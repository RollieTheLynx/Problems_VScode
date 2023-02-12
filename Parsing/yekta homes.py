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
    table = soup.find("ul", {"class": "items"})
    items = table.find_all("li", class_=False)
    links = []

    for item in items:
        info = item.find("div", {"class": "info"})
        link = info.find('a')['href']
        links.append(link)

    try:
        pagination = soup.find('ul', class_='pagination')
        next_link = pagination.find('li', class_='next').find('a')['href']
    except AttributeError:
        next_link = None
    return links, next_link


def parse_project(link):
    soup = fetch(link)
    name = soup.find('h1', class_='h1').text
    description = soup.find('div', class_='content').text
    price = soup.find('div', class_='price').text
    params_li = soup.find('ul', class_='params').find_all('li')
    image = soup.find('div', class_="main_photo").find('image')['xlink:href']
    params = {}
    for param_li in params_li:
        param_name = param_li.find_all('div')[0].text
        param_value = param_li.find_all('div')[1].text
        params[param_name] = param_value
    return name, description, price, image, params


def addToDf(link):
    def get_new_data(link, new_data):
        project_links, next_page = get_projects(link)
        for link in project_links:
            new_line = parse_project(link)
            new_data.append(new_line)
        if next_page is not None and next_page != 'javascript:void(0)':
            new_data = get_new_data(next_page, new_data)
        return new_data

    data = []
    data = get_new_data(link, data)
    df = pd.DataFrame(data, columns=['name', 'description', 'price', 'image', 'params'])
    df_params = pd.json_normalize(df['params'])  # dict params в отдельные колонки
    df = pd.concat([df, df_params], axis=1)
    df = df.drop(columns=['params'])
    return df


ongoing = 'https://yektahomes.com/ongoing-projects/'
completed = 'https://yektahomes.com/completed-projects/'
ongoing_df = addToDf(ongoing)
print(ongoing_df)
completed_df = addToDf(completed)
print(completed_df)

path = 'yekta.xlsx'
with pd.ExcelWriter(path) as writer:
    ongoing_df.to_excel(writer, sheet_name='Ongoing', index=False)
    completed_df.to_excel(writer, sheet_name='Completed', index=False)
