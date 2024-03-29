# -*- coding: utf-8 -*-
"""
In this algorithm, traverse from left and compare adjacent elements and the higher one is placed at right side. 
In this way, the largest element is moved to the rightmost end at first. 
This process is then continued to find the second largest and place it and so on until the data is sorted.
"""
from random import randrange


def make_random_list():
    randomlist = [randrange(0, 101) for n in range(0, 100)]
    return randomlist


def bubble_sort(list):

    # loop though each list item (max number of swaps?)
    for n in range(len(list)):
        swapped = False

        # loop to compare array elements,
        # except last n items (done in previous loop) and last item
        for j in range(0, len(list)-n-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

        swapped = True

        if swapped is False:
            break

    return list


randoms = make_random_list()
sorted_list = bubble_sort(randoms)
print(sorted_list)
