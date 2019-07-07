#https://hackerrank-challenge-pdfs.s3.amazonaws.com/9828-simple-array-sum-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477698&Signature=%2BBd2QjEm8GzHoqpcX9OhrJSokjg%3D&response-content-disposition=inline%3B%20filename%3Dsimple-array-sum-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum=0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
