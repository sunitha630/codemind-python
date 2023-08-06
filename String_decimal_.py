def is_decimal_string(s):
    return s.isdigit()
n=int(input())
for i in range(n):
    s=input()
    if is_decimal_string(s):
        print('True')
    else:
        print('False')
