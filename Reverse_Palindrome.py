def rev(num):
    return int(str(num)[::-1])
def is_pal(n):
    if n==rev(n):
        return True
    else:
        return False
    
n=int(input())
while (1):
    u=rev(n)
    n=n+u
    if is_pal(n)==True:
        break
print(n)

    