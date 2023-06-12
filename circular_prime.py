def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
rev=int(str(n)[::-1])
if is_prime(n) and is_prime(rev):
    print('circular prime')
elif is_prime(n) or  is_prime(rev):
    print('prime but not a circular prime')
else:
    print('not prime')