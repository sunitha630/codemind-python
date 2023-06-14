def is_prime(num):
    if num==1:
        return True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input())
l=len(str(n))
rev=int(str(n)[::-1])
if is_prime(n):
    if is_prime(rev):
        print('circular prime')
    elif is_prime(rev)==False:
        print('prime but not a circular prime')
else:
    print('not prime')