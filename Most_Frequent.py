n=int(input())
arr=list(map(int,input().split()))
l=list(set(arr))
u=[]
for i in l:
    u.append(arr.count(i))
ma=max(u)
ind=u.index(ma)
print(l[ind])