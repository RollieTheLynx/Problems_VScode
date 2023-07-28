# -*- coding: utf-8 -*-
"""
Sorted list only!

Compare the middle element of the search space with the key. 
If the key is found at middle element, the process is terminated.
If the key is not found at middle element, choose which half will be used as the next search space.
If the key is smaller than the middle element, then the left side is used for next search.
If the key is larger than the middle element, then the right side is used for next search.
This process is continued until the key is found or the total search space is exhausted.

"""
from random import randrange


def make_sorted_list(n):
    randomlist = [randrange(0, 101) for n in range(0, 100)]
    randomlist.sort()
    return randomlist


def binarySearch(arr, x):
 
    l = 0 # lower border of search
    r = len(arr) - 1 # upper border of search (index from 0 to 99 if len = 100)

    while l <= r: # while search border did not meet
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return "Not there!"

values = make_sorted_list(100)
print(values)
searched_thing = 10
position = binarySearch(values, searched_thing)
print(position)