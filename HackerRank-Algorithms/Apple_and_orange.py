#https://hackerrank-challenge-pdfs.s3.amazonaws.com/25220-apple-and-orange-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562405719&Signature=s1L4XpkUUWZuwKNZ6RISYHvydyk%3D&response-content-disposition=inline%3B%20filename%3Dapple-and-orange-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ca=0
    co=0
    for i in apples:
        d=a+i
        if d>=s and d<=t:
            ca+=1
    for i in oranges:
        d=b+i
        if d>=s and d<=t:
            co+=1
    print(ca)
    print(co)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
