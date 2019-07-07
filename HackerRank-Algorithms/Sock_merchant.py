#https://hackerrank-challenge-pdfs.s3.amazonaws.com/25168-sock-merchant-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477702&Signature=3mtypLvCoe9tQNiOhPa4uhot7%2Bw%3D&response-content-disposition=inline%3B%20filename%3Dsock-merchant-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    li=[]
    tc=0
    for i in ar:
        if i not in li:
            li.append(i)
    for i in range(len(li)):
        c=0
        for j in ar:
            if li[i]==j:
                c+=1
        if c%2==0:
            tc+=c/2
        else:
            tc+=(c-1)/2
    return int(tc)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
