#https://hackerrank-challenge-pdfs.s3.amazonaws.com/8781-a-very-big-sum-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562405582&Signature=1goyhMdkMVj2flJCpp52it4IXVs%3D&response-content-disposition=inline%3B%20filename%3Da-very-big-sum-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum=0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
