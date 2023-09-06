n=int(input())
l=list(map(int,input().split()))
ma=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[j]-l[i]>0:
            if ma<l[j]-l[i]:
                ma=l[j]-l[i]
print(ma)