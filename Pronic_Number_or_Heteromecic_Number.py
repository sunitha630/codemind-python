n=int(input())
c=0
co=0
for i in range(1,n+1):
    if n%i==0 and i*(i+1)==n:
        c+=1
    else:
        co+=1
if c>0:
    print('YES')
else:
    print('NO')
        