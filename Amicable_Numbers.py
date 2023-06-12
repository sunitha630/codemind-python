def su(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    return s
n=int(input())
num=int(input())
if su(n)==num and su(num)==n:
    print('Amicable')
else:
    print('Not Amicable')
            