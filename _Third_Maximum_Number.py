n=int(input())
l=list(map(int,input().split()))
if n==1 or n==2:
    print (l[-1])
else:
    l1=list(set(l))
    l1.sort()
    print (l1[-3])
    
