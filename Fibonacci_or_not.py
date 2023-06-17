n=int(input())
a=0
b=1
count=0
c=a+b
for i in range(0,n):
    c=a+b
    if c==n:
        count+=1
    a=b
    b=c
if count==1:
    print('True')
else:
    print('False')