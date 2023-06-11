def sqrt(num):
    return num**0.5
n=int(input())
for i in range(1,n+1):
    u=int(input())
    uu=sqrt(u)
    if uu==round(uu):
        print('True')
    else:
        print('False')