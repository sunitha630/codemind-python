def is_numeric(input_str):
    return input_str.isdigit()
n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if is_numeric(i):
            c+=1
    if(c!=0):
        print('Yes')
    else:
        print('No')
        
