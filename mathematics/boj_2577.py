# boj 2577 숫자의 개수

a = int(input())
b = int(input())
c = int(input())
res = list(str(a * b * c))

for i in range(10):
    print(res.count(str(i)))