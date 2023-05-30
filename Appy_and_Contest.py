tc=int(input())
for i in range(tc):
    n,a,b,k=map(int,input().split())
    u=(n//a)+(n//b)
    if(u>=k):
        print('Win')
    else:
        print('Lose')