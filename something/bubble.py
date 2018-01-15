#!/usr/bin/python
# -*- coding: utf-8 -*-
'''冒泡排序'''


def bubble(l):
    flag = True
    for i in range(len(l)-1, 0, -1):
        if flag:
            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
    print(l)


l = [21, 44, 2, 45, 33, 4, 3, 67, 69, 33.5]
bubble(l)


def SelSort(L):
    length = len(L)
    for i in range(length-1):
        minIdx = i
        minVal = L[i]
        j = i+1
        while j < length:
            if minVal > L[j]:
                minIdx = j
                minVal = L[j]
            j = j+1
        L[i], L[minIdx] = L[minIdx], L[i]
    print(L)


L = [1, 5, 78, 54, 84, 13, 4, 23, 46]
SelSort(L)


def bubSort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapped = True
    print(L)


L = [1, 5, 78, 54, 84, 13, 4, 23, 46]
bubSort(L)
