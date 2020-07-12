# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:32:50 2020

@author: Rollie

IMG_20190806_140621.jpg

https://pypi.org/project/exif/
"""
import webbrowser
from exif import Image

filename = input("Enter filename: ")

try:
    with open(filename, 'rb') as image_file:
        my_image = Image(image_file)
    
    if my_image.has_exif == False:
        print("No EXIF data here!")
    else:
        # формат гугла:
        # 41°24'12.2"N 2°10'26.5"E
        # https://www.google.com/maps/place/41°24'12.2"N+2°10'26.5"E/
            
        lat_deg = str(int(my_image.gps_latitude[0]))+"°"
        lat_min = str(int(my_image.gps_latitude[1]))+"'"
        lat_sec = str(my_image.gps_latitude[2])+'"'
        
        lon_deg = str(int(my_image.gps_longitude[0]))+"°"
        lon_min = str(int(my_image.gps_longitude[1]))+"'"
        lon_sec = str(my_image.gps_longitude[2])+'"'
        
        lat_sign = str(my_image.gps_latitude_ref)
        lon_sign = str(my_image.gps_longitude_ref)
        
        
        link = "https://www.google.com/maps/place/" + lat_deg + lat_min + lat_sec +lat_sign + "+" + lon_deg + lon_min + lon_sec + lon_sign
        
        webbrowser.open(link, new=2)
        
except FileNotFoundError:
    print("No such file!")
    
