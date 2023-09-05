def self_divide(n):
    c,co=0,0
    tem=n
    if n<10:
        return True
    else:
        while(n!=0):
            t=n%10
            if(t!=0 and tem%t==0):
                c+=1
            n=n//10
            co+=1
    if c==co:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if self_divide(i):
        print(i,end=" ")
        