def is_pal(num):
    if num==int(str(num)[::-1]):
        return True
    else:
        return False
num=int(input())
low=num-1
while not is_pal(low):
    low=low-1
high=num+1
while not is_pal(high):
    high=high+1
if high-num==num-low:
    print(low,high)
elif high-num>num-low:
    print(low)
else:
    print(high)