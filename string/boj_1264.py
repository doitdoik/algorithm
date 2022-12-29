v = ['a','e','i','o','u']

while True:
    cnt = 0
    s = input().lower()
    if s == '#':
        break
    for i in(s):
        if i in v:
            cnt += 1
    print(cnt)  