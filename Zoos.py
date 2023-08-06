s=(input())
zc=0
oc=0
for i in s:
    if i=='z':
        zc+=1
    elif i=='o':
        oc+=1
if(2*zc==oc):
    print('Yes')
else:
    print('No')
        