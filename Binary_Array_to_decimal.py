n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+(i*(2**(n-1)))
    n-=1
print(s)
    