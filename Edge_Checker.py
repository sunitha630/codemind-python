a,b=map(int,input().split())
if(b==a+1):
    print("Yes")
elif(a==b+1):
    print("Yes")
elif(a==1 and b==10):
    print("Yes")
elif(a==10 and b==1):
    print("Yes")
else:
    print("No")
