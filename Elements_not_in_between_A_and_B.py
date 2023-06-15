n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
found=False
for i in l:
    if i<a or i>b:
        print(i,end=" ")
        found=True
if not found:
    print(-1)