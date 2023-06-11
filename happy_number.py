n=int(input())
s=10
while s>=10:
    s=0
    while n!=0:
        r=n%10
        s=s+(r*r)
        n//=10
    n=s
if s==1 or s==7:
    print('True')
else:
    print('False')
