#https://hackerrank-challenge-pdfs.s3.amazonaws.com/32335-breaking-best-and-worst-records-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562404614&Signature=YjpRKxR8ihp7uwcrEAt%2BmnrqeEE%3D&response-content-disposition=inline%3B%20filename%3Dbreaking-best-and-worst-records-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max=scores[0]
    min=scores[0]
    ml=0
    mh=0
    l=[]
    for i in scores:
        if i>max:
            max=i
            mh+=1
        if i<min:
            min=i
            ml+=1
    l.append(mh)
    l.append(ml)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
