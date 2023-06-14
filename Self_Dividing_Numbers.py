def self_div(num):
    c=0
    co=0
    temp=num
    l=len(str(num))
    while num!=0:
        r=num%10
        if r==0:
            return False
        elif temp%r==0:
            c+=1
        else:
            co+=1
        num//=10
    if c==l:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if self_div(i):
        print(i,end=" ")
        