s=input()
su=0
for i in s:
    if i.isnumeric():
        su=su+int(i)
print(su)