n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in l:
    if i%2==0:
        ec+=1
    else:
        oc+=1
if(oc%2!=0):
    print(0)
else:
    print(1)
        
    