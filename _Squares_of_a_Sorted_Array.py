n=int(input())
l=list(map(int,input().split()))
l.sort()
u=[]
for i in l:
    k=i*i
    u.append(k)
u.sort()
print(*u)