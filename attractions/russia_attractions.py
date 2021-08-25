'''
Датасет https://www.kaggle.com/vitaliymalcev/russian-touris-attractions на карте Folium
'''

import folium
import pandas as pd 
import re

df = pd.read_csv("attractions\\tourist_attractions.csv") 
# drop rows with empty coords
df = df[df.geolocation != "Not found"]
df = df[df.geolocation != ""]

myMap = folium.Map(location=[55.796391, 49.108891], tiles="OpenStreetMap",  zoom_start=8)

for ind in df.index:
    # re.findall(r"'(.*?)'", df['geolocation'][7]) - list of coords in quotes
    print(df['name'][ind])
    print(float(re.findall(r"'(.*?)'", df['geolocation'][ind])[0]))
    print(float(re.findall(r"'(.*?)'", df['geolocation'][ind])[1]))

    folium.Marker(location=[float(re.findall(r"'(.*?)'", df['geolocation'][ind])[1]), float(re.findall(r"'(.*?)'", df['geolocation'][ind])[0])],
                    tooltip=df['name'][ind],
                    popup=df['name'][ind],
                    icon=folium.Icon(color='darkblue', icon_color = 'white', icon='image', prefix='fa')).add_to(myMap)  # https://fontawesome.com/icons/image

myMap.save("attractions.html")
