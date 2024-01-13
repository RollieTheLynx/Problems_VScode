# -*- coding: utf-8 -*-

import os, string, urllib
from bs4 import BeautifulSoup as bs
import urllib.request


def load_url(a_url):
	filehandle = urllib.request.urlopen(a_url).read()
	return filehandle

def load_html(infile):
    html = open(infile, 'rb').read()
    return html 

def get_overview_links(html):
	tuples = []
	soup = bs(html, "lxml")
	stories = soup.find_all("table", {"class" : "catalog-outer"})
	for story in stories:
		price = story.find("div", {"class" : "catalog-label catalog-label-price"})
		paid = False if price is None else True
		a = story.find("table", {"class" : "catalog-data-header"}).find_all("a")
		a_link = 'https://stulchik.cc' + a[1]['href']
		a_text = a[1].text
		author = a[2].text
		tuples.append([a_text, a_link, author, paid])
	return tuples

def retrieve_text(txt, link):
    html = load_url(link)
    soup = bs(html, "lxml")
    description = soup.find("div", {"class" : "catalog-intro"})
    if description is not None:
        description = description.text + '\n\n\n'
        txt += description
    currpagecontent = soup.find("div", {"id" : "currpagecontent"})
    paragraph = currpagecontent.find_all('p')
    for p in paragraph:
        p_text = p.get_text(strip = True)
        if len(p_text)>1:
            txt += '\n\n' + p_text
    nextPage = soup.find(lambda tag:tag.name=="a" and "следующая страница »" in tag.text.lower())
    if nextPage is not None:
        nextPage = 'https://stulchik.cc' + nextPage['href']
        txt = retrieve_text(txt, nextPage)
    return txt

def save_story(completePath, text):
    try:
        with open(completePath, 'w', encoding="utf-8") as f:
            f.write(text)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    for i in range(1,31):
        print("Page " + str(i))
        # catalogue = 'https://stulchik.cc/ras.shtml?cat=Intsest&sort=rating&page=' + str(i)
        catalogue = 'https://stulchik.cc/ras.shtml?cat=Zoofily&sort=rating&page=' + str(i)
        # catalogue = 'https://stulchik.cc/ras.shtml?cat=Molodiye&sort=rating&page=' + str(i)
        bugged = ('https://stulchik.cc/ras.shtml?rid=3969',
                  'https://stulchik.cc/ras.shtml?rid=4248',
                  'https://stulchik.cc/ras.shtml?rid=5150',
                  'https://stulchik.cc/ras.shtml?rid=3325')
        html = load_url(catalogue)
        links = get_overview_links(html)
        for title, link, author, paid in links:
            print(title, link, author)
            if paid is False and link not in bugged:
                id = link.split("rid=",1)[1]
                save_path = 'E:/zoo/'
                title = title.translate(str.maketrans('', '', string.punctuation))
                author = author.translate(str.maketrans('', '', string.punctuation))
                splittitle = title.split()
                filepath = str('_'.join(splittitle)) + '_' + id + '_' + author + '.txt'
                completePath = os.path.join(save_path, filepath)  
                if os.path.isfile(completePath) is False:
                    try:
                        text = retrieve_text('', link)
                        print('SAVING')
                        save_story(completePath, text)
                    except ValueError:
                        continue