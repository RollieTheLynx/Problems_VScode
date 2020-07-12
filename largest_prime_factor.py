# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import calendar
days = {0: "Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

read = input("Enter DD MM YYYY: ")
read = read.split(" ")
read = list(map(int, read))
#read = [int(read[0]), int(read[1]),int(read[2])]
print(days[((calendar.weekday(read[2], read[1], read[0])))]) #for year (1970–…), month (1–12), day (1–31).