n=int(input())
t=n
s=0
d=len(str(n))
while n!=0:
    r=n%10
    s=s+(r**d)
    d-=1
    n//=10
if s==t:
    print('True')
else:
    print('False')

        