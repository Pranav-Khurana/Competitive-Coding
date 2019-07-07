#https://hackerrank-challenge-pdfs.s3.amazonaws.com/21400-compare-the-triplets-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476444&Signature=nMSJxbDCbC0ufvNyB8PRllDGPFs%3D&response-content-disposition=inline%3B%20filename%3Dcompare-the-triplets-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    c=[ 0, 0]
    for i in range(3):
        if a[i]>b[i]:
            c[0]+=1
        elif a[i]<b[i]:
            c[1]+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
