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