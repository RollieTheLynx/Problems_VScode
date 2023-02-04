import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


def fetch(page):
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
        ]
    headers = {"User-Agent": random.choice(user_agent_list)}
    result = requests.get(page, headers=headers)
    # print(result.status_code)
    # print(result.headers)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    return soup


def get_projects(soup):
    links = []
    project_as = soup.find_all("a", href=True)
    for project_a in project_as:
        link = project_a['href']
        if '/en/projects/' in link:
            links.append(link)
    return links


def parse_project(link):
    soup = fetch(link)
    name = soup.find('div', class_='promo_cover_nombre ').text
    all_text = soup.text
    price = soup.find('div', class_='text-right price').text
    params_li = soup.find(id='property-section-detail').find_all('li')
    image = soup.find('img', class_="attachment-homesweet-gallery-v2 size-homesweet-gallery-v2")['src']
    return name, description, price, image, params


# def addToDf(link):
#     def get_new_data(link, new_data):
#         project_links, next_page = get_projects(link)
#         for link in project_links:
#             new_line = parse_project(link)
#             new_data.append(new_line)
#         if next_page is not None:
#             new_data = get_new_data(next_page, new_data)
#         return new_data

#     data = []
#     data = get_new_data(link, data)
#     df = pd.DataFrame(data, columns=['name', 'description', 'price', 'image', 'params'])
#     df_params = pd.json_normalize(df['params'])  # dict params в отдельные колонки
#     df = pd.concat([df, df_params], axis=1)
#     df = df.drop(columns=['params'])
#     return df


# sale = 'https://terigroup.ru/properties/?filter-contract=SALE'
# ongoing_df = addToDf(sale)
# print(ongoing_df)

# path = 'teri group.xlsx'
# with pd.ExcelWriter(path) as writer:
#     ongoing_df.to_excel(writer, sheet_name='Ongoing', index=False)





link = 'https://www.kronoshomes.com/en/projects/'
soup = fetch(link)
projects = ['https://www.kronoshomes.com/' + s for s in get_projects(soup)]