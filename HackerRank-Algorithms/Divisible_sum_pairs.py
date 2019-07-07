#https://hackerrank-challenge-pdfs.s3.amazonaws.com/21634-divisible-sum-pairs-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476810&Signature=9EKfJefRPP33%2BEQ5RxeNFnXUNa4%3D&response-content-disposition=inline%3B%20filename%3Ddivisible-sum-pairs-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j])%k==0:
                c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
