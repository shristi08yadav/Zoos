s = str(input())
a = 0
b = 0
for i in s:
    if "z"==i:
        a+=1
    if "o"==i:
        b+=1    
if 2*a==b:
    print("Yes")
else:
    print("No")        
