# -*- coding: utf-8 -*-

import os, string, urllib
from bs4 import BeautifulSoup as bs
import urllib.request
import urllib.error


def load_url(a_url):
	try:
		filehandle = urllib.request.urlopen(a_url).read()
		return filehandle
	except urllib.error.HTTPError:
		print(urllib.error.HTTPError.code)
		return '404'

def get_overview_links(html):
	tuples = []
	soup = bs(html, "lxml")
	paragraph = soup.find_all("div", {"class" : "b-sl-item-r w-34t"})
	for td in paragraph:
		a = td.find_all("a")[0]
		a_link = a['href']
		a_text = a.text
		span = td.find('span', {'class' : 'b-sli-rating'})
		try:
			rating = float(span.text)
		except AttributeError: rating = 0
		author = td.find('span', {'class' : 'b-sli-author'}).text.removeprefix('\n\t\t\t\t\tby\xa0')
		tuples.append([a_text, a_link, rating, author])
	return tuples

def retrieve_text(txt, link):
    html = load_url(link)
    if html != '404':
        soup = bs(html, "lxml")
        description = soup.find("div", {"class" : "bn_B"})
        if description is not None:
            description = description.text + '\n\n\n'
            txt += description
        uebersicht = soup.find("div", {"class" : "aa_ht"}).find_all('p')
        for p in uebersicht:
            p_text = p.text
            txt += '\n\n' + p_text
        nextPage = soup.find("a", {"class" : "l_bJ l_bL"})
        if nextPage is not None:
            nextPage = 'https://www.literotica.com' + nextPage['href']
            txt = retrieve_text(txt, nextPage)
        return txt

def save_erotica(completePath, text):
    try:
        with open(completePath, 'w') as f:
            f.write(text)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    counter = 0
    for i in range(1,269):
    	#literotica_link = "https://www.literotica.com/top/most-read-erotic-stories/alltime/?page=" + str(i)
        #literotica_link = 'https://www.literotica.com/top/most-read-erotic-stories/last-12-months/?page=' + str(i)
        #literotica_link = 'https://www.literotica.com/top/most-read-erotic-stories/last-30-days/?page=' + str(i)
        literotica_link = 'https://www.literotica.com/c/taboo-sex-stories/' + str(i) + '-page'
        #literotica_link = 'https://www.literotica.com/c/erotic-horror/' + str(i) + '-page'
        #literotica_link = 'https://www.literotica.com/c/group-sex-stories/' + str(i) + '-page'
        #literotica_link = 'https://www.literotica.com/c/science-fiction-fantasy/' + str(i) + '-page'
        #literotica_link = 'https://www.literotica.com/c/lesbian-sex-stories/' + str(i) + '-page'
        #literotica_link = 'https://www.literotica.com/c/gay-sex-stories/' + str(i) + '-page'
        print('Page ' + str(i))
        print(literotica_link)
        html = load_url(literotica_link)
        links = get_overview_links(html)
        for title, link, rating, author in links:
            print(counter, title, link, rating, author)
            counter += 1
            save_path = 'E:/incest/'
            title = title.translate(str.maketrans('', '', string.punctuation))
            author = author.translate(str.maketrans('', '', string.punctuation))
            splittitle = title.split()
            filepath = str('_'.join(splittitle)) + '_' + author + '.txt'
            completePath = os.path.join(save_path, filepath)  
            if os.path.isfile(completePath) is False:
                try:
                    text = retrieve_text('', link)
                    print('SAVING')
                    save_erotica(completePath, text)
                except ValueError:
                    continue