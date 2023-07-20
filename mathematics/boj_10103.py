# boj 10103 주사위 게임
n = int(input())
x = 100
y = 100
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        y -= a
    if a < b:
        x -= b
print(x)
print(y)

      


     