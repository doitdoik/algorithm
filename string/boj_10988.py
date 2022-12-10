s = input()
x = 1

for i in range(len(s)//2):
    if s[i] != s[-i-1]: 
        print(0)
        x = 0
        break

if x == 1: 
    print(x)