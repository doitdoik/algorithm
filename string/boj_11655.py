s = input()
res = ''

for i in s:
    if i.isupper():
        if (65 <= ord(i) <= 77):
            res += chr(ord(i) + 13) 
        else:
            res += chr(ord(i) - 13)  
    elif i.islower():
        if (97 <= ord(i) <= 109):
            res += chr(ord(i) + 13) 
        else:
            res += chr(ord(i) - 13) 
    else:
        res += i
        
print(res)