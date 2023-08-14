r=int(input())
c=int(input())
il=[]
ol=[]
s=0
for i in range(r):
    il=list(map(int,input().split()))
    ol.append(il)
for i in range(r):
    for j in range(c):
        s=s+ol[i][j]
print(s)
