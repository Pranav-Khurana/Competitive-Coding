#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    t=0
    for i in range(max(a),min(b)+1):
        ca=0
        cb=0
        for j in a:
            if i%j==0:
                ca+=1
        if ca==len(a):
            for j in b:
                if j%i==0:
                    cb+=1
        if cb==len(b):
            t+=1
    return t
        
            
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
