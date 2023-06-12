def is_aut(n):
    sq=n*n
    if str(n)==str(sq)[-len(str(n)):]:
        return True
    else:
        return False
n=int(input())
if is_aut(n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    
