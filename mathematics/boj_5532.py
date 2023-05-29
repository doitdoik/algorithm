# boj 5532 방학 숙제
import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = math.ceil(a / c)
m = math.ceil(b / d)

print(l - max(k, m))