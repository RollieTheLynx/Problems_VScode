# - ExercisesModuleEnd1.py *- coding: utf-8 -*-
""" Find and correct all the errors in the following Python functions.
    To run one, click in the cell (between two lines) and type Ctrl-Enter for
    Windows or Command-Return for a Mac.  Then enter the name of the function
    into the IPython console.  For example, to run the first one enter
    print_phrase() and press return.
"""
""" 
Exercise 1 
"""
#%%
def print_phrase():
    phrase = "Now is the time"
    print (phrase)
#%%
""" 
Exercise 2
"""
#%%
def favorite_sport():
    sport = "boob"
    print("Your favorite sport is",sport)
#%%
""" 
Exercise 3 
"""
#%%
def username(yourname):
    print("Your name is",yourname)
#%%
"""
Exercise 4
"""
#%%
def compare_numbers(x,y):
    if x == y:
        print("they are equal")
    else:
        print(x, "and", y, 'are not equal')
#%%
        """
Exercise 5
"""
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print ('Counting from 5 through 100 in steps of 5')
    ct = 5
    while ct < 100:
        print(ct, end = " ")
        ct = ct + 5
#%%