#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(n,a):
    li=[]
    for i in range(n-1,-1,-1):
        li.append(a[i])
    return li
      
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr_count,arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
