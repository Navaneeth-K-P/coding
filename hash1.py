#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def insert(d,s,l):
    h=0
    for i in range(0,len(s)):
        h+=(h*256)+ord(s[i])
    h=h%l
    while(d[h]!=''):
        h=(h+1)%l
    d[h]=s
    return(d)

def find(d,m,l):
    h=0
    for i in range(0,len(m)):
        h+=(h*256)+ord(m[i])
    h=h%l
    if(d[h]==m):
        return(0)
    else:
        r=h
        h=(h+1)%l
        while(d[h]!=m):
            if(d[h]=='' or h==r):
                return(1)
            else:
                h=(h+1)%l
        return(0)

def checkMagazine(magazine, note):
    # Write your code here
    l=8*len(magazine)
    d=['']*l
    for m in magazine:
        d=insert(d,m,l)
    flag=0
    for n in note:
        flag=find(d,n,l)
        if(flag==1):
            break
        else:
            d[d.index(n)]=''
    if(flag==0):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
