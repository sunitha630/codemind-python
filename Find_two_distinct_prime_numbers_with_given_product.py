def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
n=int(input())
for i in range(1,n-1):
    if n%i==0 and is_prime(i):
        print(i,n//i)
        break
else:
    print(-1)
    