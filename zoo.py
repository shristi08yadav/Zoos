"""
You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.
Print Yes if the input word can be considered as the string zoo otherwise, print No.
"""
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
