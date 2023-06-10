i,r,k=map(int,input().split())
c=0
for o in range(i,r+1):
    if o%k==0:
        c+=1
print(c)