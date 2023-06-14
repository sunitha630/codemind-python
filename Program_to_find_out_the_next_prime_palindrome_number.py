def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def is_pal(num):
    if num==int(str(num)[::-1]):
        return True
    else:
        return False
n=int(input())
i=1
while(1):
    n=n+1
    if is_prime(n) and is_pal(n):
        print(n)
        break
    else:
        i+=1
        
    
    