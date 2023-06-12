def is_pal(num):
    if num==int(str(n)[::-1]):
        return True
    else:
        return False
tc=int(input())
for i in range(1,tc+1):
    n=int(input())
    if is_pal(n):
        print('True')
    else:
        print('False')