#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hgs=[]
    x=0
    for _ in range(4):  
        m=0
        for i in range(4):
            s=0
            for j in range(m,m+3):
                s+=arr[0+x][j]
                s+=arr[2+x][j]
            s+=arr[1+x][i+1]
            hgs.append(s)
            m+=1
        x+=1
    return max(hgs)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
