s = list(input().split('-'))

for i in range(len(s)) :
    s[i] = sum(map(int,s[i].split('+')))

res = s[0]
for i in range(1,len(s)) :
    res -= s[i]

print(res)