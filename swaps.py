#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    return(arr)

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    print(arr)
    j=0
    c=sorted(arr)
    while j<len(arr):
        if(arr==c):
            break
        for i in range(0,len(arr)):
            k=arr[arr[i]-1]
            if(arr==c):
                break
            if(arr[i]==i+1):
                continue
            elif(i+1==k):
                arr=swap(arr,i,arr[i]-1)
                #print('1')
                #print(arr)
                count+=1
        if(arr[j]==j+1):
            j+=1
        else:
            k=arr.index((arr.index(j+1))+1)
            arr=swap(arr,j,k)
            count+=1
    return(count)

if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
