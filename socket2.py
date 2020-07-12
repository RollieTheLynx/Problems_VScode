# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:11:34 2020

@author: Rollie
"""


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode() #\r\n\r\n = enter enter
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) <1 ):
        break
    print(data.decode()) #assumes utf-8 or ascii
mysock.close()




#%%
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") #file handle in quotes
for line in fhand:
    print(line.decode().strip())