n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
su=0
for i in l:
    if i<a or i>b:
        su=su+i
print(su)