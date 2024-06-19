# -*- coding: utf-8 -*-
"""task05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TIANZu63SSGyVNrtAr3MdOaSI1qyKaGr
"""

input = open('input5.txt','r')
output = open('output5.txt','w')

n = int(input.readline())
arr = list(map(int,input.readline().split()))

def Quick(arr,low,high):
    if len(arr)<=1: return arr
    if low < high:
        p = partition(arr,low,high)
        Quick(arr,low,p-1)
        Quick(arr,p+1,high)
    return arr

def partition(arr,low,high):
    piv = arr[low]
    i = low
    for j in range(i+1, high+1):
        if arr[j] <= piv:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i] , arr[low] = arr[low] , arr[i]
    return i

Quick(arr,0,n-1)
for i in range(n):
    output.write(f'{arr[i]} ')
input.close()
output.close()

