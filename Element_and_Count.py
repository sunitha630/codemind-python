n=int(input())
l=list(map(int,input().split()))
u=[]
for i in l:
    if i not in u:
        u.append(i)
r=[]
for i in u:
    y=l.count(i)
    r.append(y)
for i in range(len(r)):
    print(u[i],r[i],end=" ")