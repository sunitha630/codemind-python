num,n=map(int,input().split())
st=str(num)
f_n=st[:n]
l_n=st[-n:]
print(abs(int(f_n)-int(l_n)))
