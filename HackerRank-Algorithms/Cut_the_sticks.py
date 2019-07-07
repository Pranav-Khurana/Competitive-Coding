#https://hackerrank-challenge-pdfs.s3.amazonaws.com/1957-cut-the-sticks-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476582&Signature=VshzfcHQAGPv5KIC1xNsob8t%2Fck%3D&response-content-disposition=inline%3B%20filename%3Dcut-the-sticks-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(ls):
    rls=[]
    while(len(ls)):
        sm=min(ls)
        c=0
        for i in range(len(ls)):
            ls[i]-=sm
            c+=1
        while ls.count(0):
            ls.remove(0)
        rls.append(c)
    return rls



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
