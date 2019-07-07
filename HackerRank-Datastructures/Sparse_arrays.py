# https://hackerrank-challenge-pdfs.s3.amazonaws.com/13724-sparse-arrays-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562480151&Signature=%2BiTugBtXDwpEmCP3VtaH3nZ6PZY%3D&response-content-disposition=inline%3B%20filename%3Dsparse-arrays-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    res=[]
    for i in  queries:
        res.append(strings.count(i))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
