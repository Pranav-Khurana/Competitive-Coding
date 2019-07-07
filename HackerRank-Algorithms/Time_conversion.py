#https://hackerrank-challenge-pdfs.s3.amazonaws.com/8649-time-conversion-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477844&Signature=uDe2OLe%2FB5yxfQQDMb6cUdVPThs%3D&response-content-disposition=inline%3B%20filename%3Dtime-conversion-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import os
import sys


def timeConversion(s):
    t=s[8:]
    if t.lower()=='pm' and s[:2]!='12':
        y=12+int(s[:2])
        s=s.replace(s[:2],str(y))
    elif t.lower()=='am' and s[:2]=='12':
        s=s.replace(s[:2],'00')
    return s[:8]



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
