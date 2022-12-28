cnt = 0
s = input()

for v in ('a', 'e', 'i', 'o', 'u'):
    cnt += s.count(v)
    
print(cnt)