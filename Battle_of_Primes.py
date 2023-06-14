def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+2):
        if num%i==0:
            return False
    return True
a=int(input())
b=int(input())
n=a+b
i=1
while(1):
    n=n+1
    if is_prime(n):
        print(n-(a+b))
        break
    else:
        i=i+1