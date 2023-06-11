import math
n=int(input())
temp=n
s=0
while temp>0:
    r=temp%10
    s=s+math.factorial(r)
    temp//=10
if s==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')
