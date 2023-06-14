def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input())
low=n
while not is_prime(low):
    low=low-1
high=n
while not is_prime(high):
    high=high+1
if high-n>=n-low:
    print(abs(n-low))
else:
    print(abs(n-high))
    