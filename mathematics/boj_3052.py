# boj 3052 나머지

arr = []
for i in range(10):
    n = int(input())
    if n % 42 not in arr:
        arr.append(n % 42)

print(len(arr))