n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
if(n%2==0):
    u=(n//2)
    print(s[u])
else:
    uu=(n//2)
    print(s[uu])
    