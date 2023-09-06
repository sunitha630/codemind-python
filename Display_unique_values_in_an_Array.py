n=int(input())
arr=list(map(int,input().split()))
uni=[]
for i in arr:
    if arr.count(i)==1:
        uni.append(i)
if len(uni)==0:
    print(-1)
else:
    print(*uni)