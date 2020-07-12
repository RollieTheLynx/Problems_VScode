# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:11:47 2020

@author: Rollie

Write a program to find the shortest routing and distance between two Alabama cities using the following distance table.

You are not allowed to use any other manually computed distances in your program.

Alabaster-Birmingham 24 miles
Alabaster-Montgomery 71 miles
Birmingham-Huntsville 103 miles
Birmingham-Tuscaloosa 59 miles
Demopolis-Mobile 141 miles
Demopolis-Montgomery 101 miles
Demopolis-Tuscaloosa 65 miles
Mobile-Montgomery 169 miles
Montgomery-Tuscaloosa 134 miles

Example 1:
￼Enter city #1: Demopolis
Enter city #2: Birmingham
Shortest routing and distance:
Demopolis-Tuscaloosa-Birmingham, 124 miles

Example 2:
Enter city #1: Mobile
Enter city #2: Huntsville
Shortest routing and distance: Mobile-Montgomery-Alabaster-Birmingham-Huntsville, 367 miles
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""
all_links = [("alabaster", 24, "birmingem"), ("alabaster", 71, "montgomery"), ("birminghem", 103, "huntsville"),("birminghem", 59, "tuscaloosa"), ("demopolis", 141, "mobile") , ("demopolis", 101, "montgomery"), ("demopolis", 65, "tuscaloosa"), ("mobile", 169, "montgomery"), ("montgomery", 134, "tuscaloosa")]
nextoption = []
distancesofar = 0

def NextLink(prevtown,distancesofar):
    for i in all_links:
        if prevtown == i[0]:
            nextoption.append((i[2], i[1]))

starttown = input("Enter city #1: ").lower()

NextLink(starttown)
print(nextoption)

for option in nextoption:
    NextLink(option)