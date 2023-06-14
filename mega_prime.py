def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input())
l=len(str(n))
c=0
if is_prime(n):
    while n!=0:
        r=n%10
        if is_prime(r):
            c+=1
        n//=10
if c==l:
    print('Mega Prime')
else:
    print('Not Mega Prime')
            
    