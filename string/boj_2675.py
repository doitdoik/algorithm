t = int(input())

for _ in range(t):
    r, s = input().split()
    res = ''
    for i in s:
        res += int(r) * i
    print(res)