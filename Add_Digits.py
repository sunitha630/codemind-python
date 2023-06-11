n=int(input())
su=10
while su>=10:
    su=0
    while n!=0:
        r=n%10
        su=su+r
        n//=10
    n=su
print(n)
    