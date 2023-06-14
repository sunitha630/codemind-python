def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
c=0
co=0
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if is_prime(i):
            co+=1
print(abs(c-co))
        