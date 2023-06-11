n=int(input())
l=list(map(int,input().strip().split()))
u=int(input())
for i in l:
    if i+u>=max(l):
        print('True',end=" ")
    else:
        print('False',end=" ")
    