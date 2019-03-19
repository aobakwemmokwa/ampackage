# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:37:06 2019

@author: Aobakwe Mmokwa
"""

from random import randint

def bubble_sort(items):

    """
    sort items of a list using bubble sort.
        bubble sort runs through a list checking items and swapping them if
        required:
            example
            [4, 1, 2, 3]
            [1, 4, 2, 3]
            [1, 2, 4, 3]
            [1, 2, 3, 4]

    Args:
        A list of items to sort
    returns:
        A sorted list in ascending order
    """

    for i in range(len(items) - 1, 0, -1):

        for j in range(i):

            if items[j] > items[j + 1]:

                items[j], items[j + 1] = items[j + 1], items[j]

    return items

def merge_sorted_lists(list1, list2):

    """
    Merge list1 and list2 returns one sorted list

    Args:
        list1 (list): first sorted list
        list2 (list): second sorted list
    returns:
        (list): A sorted list from the two lists
    """

    sorted_list = []

    while list1 and list2:
        if list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))

    sorted_list.extend(list1)
    sorted_list.extend(list2)

    return sorted_list


def merge_sort(items):

    """
    sort items of a list using merge sort.

        Sort divides the list into multiple sublists and continuously merge
        them together and further diving until it is sorted

    Args:
        A list of items to sort
    returns:
        A sorted list in ascending order
    """

    if len(items) <= 1:
        return items

    left = items[0: int(len(items)/2)]          #variables to divide the list by half
    right = items[int(len(items)/2) :]          #each contains the half of the list

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_lists(left, right)

def quick_sort(items):

    """
    sort items of a list using merge sort.
        Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
        It picks an element as pivot and partitions the given array around
        the picked pivot.

    Args:
        A list of items to sort
    returns:
        A sorted list in ascending order
    """

    if len(items) <= 1:
        return items

    pivot = items[randint(0, len(items) - 1)]       #Choose a random number as pivot
    left = []
    right = []
    if len(items) <= 1:
        return items

    for i in items:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    left = quick_sort(left)
    right = quick_sort(right)

    return merge_sorted_lists(left, right)
