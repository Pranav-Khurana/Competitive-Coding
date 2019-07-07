#https://hackerrank-challenge-pdfs.s3.amazonaws.com/127-find-digits-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476984&Signature=Ekw%2B%2BEU6QmkN5NwEc6QsZlozSD8%3D&response-content-disposition=inline%3B%20filename%3Dfind-digits-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    no=n
    c=0
    while no>0:
        d=no%10
        if d!=0 and n%d==0:
            c+=1
        no//=10
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
