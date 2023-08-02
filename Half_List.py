n=int(input())
l=list(map(int,input().split()))
li=l[n-1:n//2-1:-1]
lii=l[:n//2]
print(*li+lii)