# -*- coding: utf-8 -*-
from bisect import bisect_left
import array
from difflib import ndiff

def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first+last)//2
        if a_list[mid] == n:
            return True
        else: 
            if n < a_list[mid]:
                last = mid - 1
            else: 
                first = mid + 1
    return False

def binary_seach_1(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i]
            i = i - 1
        a_list[i] = value
    return a_list

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list

# используются переменные first и last, чтобы отслежиать начало и конец списка

a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(a_list, 4))

unsorted_list = ['mouse','word','house','world','me','I','horse','kill','kiss']
sorted_list = sorted(unsorted_list)
print(binary_search(sorted_list, 'wod'))

s1 = "Emperor Octavian"
s2 = "Captain over Rome"
print(is_anagram(s1,s1))

nl = [c for c in "buy 1 get 2 free" if c.isdigit()][-1] # Списковое включение
print(nl)


arr = array.array("f", (1.0, 1.5, 2.0, 2.5)) # два параметра - тип данных для массива и список со значениями
print(arr[1])