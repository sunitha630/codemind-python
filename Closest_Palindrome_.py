def pal(num):
    if num==int(str(num)[::-1]):
        return True
    else:
        return False
n=int(input())
high=n+1
while not pal(high):
    high=high+1
low=n-1
while not pal(low):
    low=low-1
if high-n==n-low:
    print(low,high)
elif high-n>n-low:
    print(low)
else:
    print(high)