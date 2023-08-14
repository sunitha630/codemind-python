def num_count(num):
    c=0
    while num!=0:
        t=num%10
        c+=1
        num=num//10
    return c
n=int(input())
l=list(map(int,input().split()))
cc=0
for i in l:
    k=num_count(i)
    if k%2==0:
        cc+=1
print(cc)