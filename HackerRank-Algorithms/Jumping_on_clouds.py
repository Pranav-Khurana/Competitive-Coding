#https://hackerrank-challenge-pdfs.s3.amazonaws.com/20832-jumping-on-the-clouds-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477131&Signature=V%2FBapELjhCMf9B%2B7Im4Ym7rr%2FNw%3D&response-content-disposition=inline%3B%20filename%3Djumping-on-the-clouds-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    i=0
    while i+2<len(c) or i+1<len(c):
        if i+2<len(c) and c[i+2]==0:
            count+=1
            i+=2
        elif c[i+1]==0:
            count+=1
            i+=1
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
