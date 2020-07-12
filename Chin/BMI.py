# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:41:10 2020

@author: Rollie
The Python implementation of the classic problem is used to practice to improve the programming thinking and ability
 although it may be more convenient to solve after learning the more data structure such as sequence. If you want to 
 learn programming well, you should practice a lot. Cheer up and good luck ^_^

1．The Body Mass Index (BMI) is an internationally accepted standard for measuring the degree of obesity and health
of a person. The formula is BMI = the weight/height (kg/m2). The adult BMI value in China is defined as:

Too thin: < 18.5

Normal: 18.5-23.9

Overweight: 24-27.9

Fat: >= 28

Please enter the weight and height, and output the corresponding BMI value and weight obesity judgment result.

[input sample]

60,1.6

[output sample]

Your BMI is 23.4

normal

[tips]

The weight and height can be got by the input statement of "weight, height = eval(input())".
"""


height = int(input("Input height in cm\n"))
weight = float(input("Input weight in kg\n"))
bmi = weight/((height/100)**2)
print(round(bmi,2))
if bmi <18.5:
    print("Too thin")
elif bmi < 24:
    print("normal")
elif bmi < 28:
    print("Overweight")
else:
    print("Obese")