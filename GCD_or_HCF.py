a,b=map(int,input().split())
m=min(a,b)
while 1:
    if a%m==0 and b%m==0:
        break
    else:
        m-=1
print(m)