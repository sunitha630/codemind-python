def is_adam(n):
    sq=n*n
    rev=int(str(sq)[::-1])
    rev_n=int(str(n)[::-1])
    sq_re_n=rev_n*rev_n
    return sq==int(str(sq_re_n)[::-1])
n=int(input())
if is_adam(n):
    print('True')
else:
    print('False')