import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    a, b = map(str, input().split())
    x = sorted(a)
    y = sorted(b)

    if x == y:
        print(a, "&", b, "are anagrams.")
    else:
        print(a, "&", b, "are NOT anagrams.")