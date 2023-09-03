n=int(input())
st=str(n)
l=[]
for i in st:
    u=st.count(i)
    l.append(u)
for i in l:
    if i!=1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')
    
    