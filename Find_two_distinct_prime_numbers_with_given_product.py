def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=0
n=int(input())
for i in range(1,int(n**0.5)+1):
    if n%i==0 and is_prime(i) and is_prime(n//i) and i!=(n//i):
        print(i,n//i)
        c+=1
if c==0:
    print(-1)
        
    