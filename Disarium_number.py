n=int(input())
l=len(str(n))
s=0
temp=n
while n!=0:
    r=n%10
    s=s+(r**l)
    l=l-1
    n//=10
if temp==s:
    print('True')
else:
    print('False')

    
        