s = int(input())
n = 1
res = 0

for i in range(1, s+1) : 
    if s - i < 0 :
        break
    s -= i
    res = i

print(res)



