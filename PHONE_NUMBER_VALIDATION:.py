num=int(input())
c=0
co=0
while num!=0:
    r=num%10
    c+=1
    if c>=10 and r==0:
        co+=1
    num//=10
if c<10 or co>0:
    print('Invalid')
else:
    print('Valid')
    

        