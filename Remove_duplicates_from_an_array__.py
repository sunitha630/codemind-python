n=int(input())
l=list(map(int,input().split()))
u=list(set(l))
for i in u:
    print(i,end=" ")
    