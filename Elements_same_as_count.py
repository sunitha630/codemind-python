n=int(input())
a=list(map(int,input().split()))
d=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
            if i!=j:
                a[j]=0
    if c==a[i]:
        print(c,end=" ")
        d+=1
if d==0:
    print(-1)
        