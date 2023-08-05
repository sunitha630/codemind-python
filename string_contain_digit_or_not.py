def is_numeric(input_str):
    return input_str.isdigit()
c=0
s=input()
for i in s:
    if is_numeric(i):
        c+=1
if(c!=0):
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")