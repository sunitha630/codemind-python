n=int(input())
l=list(map(int,input().strip().split()))
s=0
su=0
for i,n in enumerate(l):
    if i%2==0:
        s+=l[i]
    elif i%2!=0:
        su+=l[i]
if((s-su)==0):
    print('YES')
else:
    print('NO')