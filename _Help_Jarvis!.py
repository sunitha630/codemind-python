n=int(input())
for i in range(n):
    k=int(input())
    k_str=str(k)
    l=[]
    for j in k_str:
        k_num=int(j)
        l.append(k_num)
    l.sort()
    c=0
    for k in range(0,len(l)-1):
        if abs(l[k]-l[k+1])==1:
            c+=1
    if c==len(l)-1:
        print('YES')
    else:
        print('NO')
                
    
    