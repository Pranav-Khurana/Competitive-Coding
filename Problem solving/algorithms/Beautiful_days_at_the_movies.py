#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    d=0
    for x in range(i,j+1):
        no=x
        rev=0
        rm=0
        while(no):
            rm=no%10
            rev=rev*10+rm
            no=no//10
        if abs(x-rev)%k==0:
            d+=1
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
