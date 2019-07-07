#https://hackerrank-challenge-pdfs.s3.amazonaws.com/30508-grading-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477041&Signature=bEhSAmGVFralEdFhNJg50SXuY4A%3D&response-content-disposition=inline%3B%20filename%3Dgrading-English.pdf&response-content-type=application%2Fpdf
#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]>=38:
            if grades[i]%5>2:
                grades[i]+=5-(grades[i]%5)
    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
