#https://hackerrank-challenge-pdfs.s3.amazonaws.com/30377-day-of-the-programmer-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476586&Signature=4SUHlTPKISLrEKpUxf8tZLANbT4%3D&response-content-disposition=inline%3B%20filename%3Dday-of-the-programmer-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(year):
    if year<=1917:
        if year%4==0:
            return("12.09."+str(year))
        else:
            return("13.09."+str(year))
    elif year==1918:
        return("26.09.1918")
    else:
        if year%4==0 and year%100!=0 or year%400==0:
            return("12.09."+str(year))
        else:
            return("13.09."+str(year))

    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return("12.09."+str(year))
            else:
                return("13.09."+str(year))
        else:
            return("12.09."+str(year))
    else:
        return("13.09."+str(year))
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = solve(year)

    fptr.write(result + "\n")

    fptr.close()
