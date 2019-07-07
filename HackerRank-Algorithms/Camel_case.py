#https://hackerrank-challenge-pdfs.s3.amazonaws.com/22578-camelcase-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476347&Signature=%2FAyf3o2JhcMBlM17CQJz%2BzZ2Wgk%3D&response-content-disposition=inline%3B%20filename%3Dcamelcase-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    c=1
    for i in s:
        if i.isupper():
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
