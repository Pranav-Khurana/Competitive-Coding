#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sl=0
    vc=0
    m=0
    for i in s:
        if i=='U':
            sl+=1
        if i=='D':
            sl-=1
        if sl<0 and m==0:
            vc+=1
            m=-5
        if sl>=0:
            m=0
    return vc
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
