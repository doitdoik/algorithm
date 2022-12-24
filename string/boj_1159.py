n = int(input())
arr = []

for _ in range(n):
    f = input()
    arr.append(f[0])

first_name = set(arr)
res = []

for i in first_name:
    if arr.count(i) >= 5:
        res.append(i)

if len(res) > 0:
    print(''.join(sorted(res)))
else:
    print("PREDAJA")