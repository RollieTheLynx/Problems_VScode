# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os

with open("C:\\Users\\Mike\\Documents\\Python_Scripts\\Problems_VScode\Parsing\\Allnair\\1677.html", encoding="utf8") as page:
    soup = BeautifulSoup(page, 'html.parser')

# print(soup)
projectName = soup.find('div', {'class' : 'LinesEllipsis'})
print(projectName.get_text())

devloperName = soup.find('span', {'class' : '_root_12tyz_1 _sizeXS_12tyz_9 _grayColor_1gsgo_40'})
print(devloperName.get_text())

districtName = soup.find('span', {'class' : '_root_12tyz_1 _sizeXS_12tyz_9'})
print(districtName.get_text())

#TODO must be a better way
allnairLink = 'https://alnair.ae/app/view/' + os.path.basename(page.name).split('.')[0]
print(allnairLink)

AEDrange = soup.find('span', {'class' : '_root_12tyz_1 _sizeXS_12tyz_9 text-right'})
print(AEDrange.get_text())

completionDate = soup.find('button', {'class' : '_baseButton_1epn5_1 _primary_16jt3_39 _medium_11a6w_11 _text_16jt3_79 _detailButton_qp4f8_20'})
print(completionDate.get_text())

percentageComplete = soup.find('div', {'class' : '_root_12tyz_1 _sizeS_12tyz_13 _progressLabel_qp4f8_16'})
print(percentageComplete.get_text())

options = soup.find_all('div', {'class' : '_hasTypicalLayouts_1jjfh_15'})
optionsDict = {}
bedroomsList = []
areasList = []

for option in options:
    bedrooms = option.find('div', {'class' : '_title_rryvf_42'})
    rooms = int(bedrooms.get_text().split()[0])
    bedroomsList.append(rooms)
    area = option.find('span', {'class' : '_root_12tyz_1 _sizeXS_12tyz_9'})
    areaRange = area.get_text().rstrip(' m²').split(' —')
    # optionData = (rooms, float(areaRange[0]), float(areaRange[1])) # (bedrooms, min area, max area)
    areasList.append(float(areaRange[0]))
    areasList.append(float(areaRange[1]))
min_bedrooms = min(bedroomsList)
max_bedrooms = max(bedroomsList)
min_area = min(areasList)
max_area = max(areasList)
print(min_bedrooms)
print(max_bedrooms)
print(min_area)
print(max_area)