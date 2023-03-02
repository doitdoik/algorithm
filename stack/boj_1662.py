# boj 1662 압축

s = str(input())
tmp = ''
stack = []
l = 0
for i in s :
    if ord(i) >= 48 and ord(i) <= 57: 
        tmp, l = i, l+1
    elif i == '(' : 
        stack.append([tmp, l-1])
        l = 0
    elif i == ')' : 
        n, p = stack.pop() 
        l = int(n)*l+p 
print(l)