n=int(input())
l=list(map(int,input().split()))
l1,l2,r_v=[],[],[]
u=n//2
if n%2!=0:
    l1=l[:u+1]
    l2=[0]+l[u+1:]
    r_v=l2[::-1]
    for i in range((n//2)+1):
        print(l1[i],r_v[i],end=" ")
else:
    l1=l[:u]
    l2=l[u:]
    r_v=l2[::-1]
    for i in range(u):
        print(l1[i],r_v[i],end=" ")

    