n=int(input())
s=0
p=1
while n!=0:
    r=n%10
    s=s+r
    p=p*r
    n//=10
print(abs(s-p))