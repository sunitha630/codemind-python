def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
u=int(input())
for i in range(1,u+1):
    num=int(input())
    low=num
    while not is_prime(low):
        low=low-1
    high=num
    while not is_prime(high):
        high=high+1
    if high-num>=num-low:
        print(low)
    else:
        print(high)
    
        