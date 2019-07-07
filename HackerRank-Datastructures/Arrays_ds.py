#https://hackerrank-challenge-pdfs.s3.amazonaws.com/13579-arrays-ds-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562479913&Signature=A0VIjPNscp2CRePSD1qM4Pb%2FF90%3D&response-content-disposition=inline%3B%20filename%3Darrays-ds-English.pdf&response-content-type=application%2Fpdf
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
