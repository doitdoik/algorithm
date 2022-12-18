import sys 

input = sys.stdin.readline
a, b, c, d = map(str, input().strip().split())
ab = a + b
cd = c + d
res = int(ab) + int(cd)

print(res)