n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    l=l+[0]
else:
    l=l
print(*l)