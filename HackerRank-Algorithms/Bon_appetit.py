#https://hackerrank-challenge-pdfs.s3.amazonaws.com/24060-bon-appetit-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562406181&Signature=wP3fYOaEe4enS72PgBmN5HrbjbY%3D&response-content-disposition=inline%3B%20filename%3Dbon-appetit-English.pdf&response-content-type=application%2Fpdf
# Enter your code here. Read input from STDIN. Print output to STDOUT

#input process
input_line1 = input().split()
n = int(input_line1[0])
b = int(input_line1[1])
bill = list(map(int, input().rstrip().split()))
r = int(input())

#algo process
s=0
for i in range(n):
    if i==b:
        continue
    s+=bill[i]
s/=2
s=int(s)
if s==r:
    print('Bon Appetit')
else:
    print(str(r-s))
