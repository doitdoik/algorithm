# boj 3053 택시 기하학
import math

r = int(input())
ur = math.pi * r * r
tr = (2*r) * (2*r) / 2

print(round(ur, 6))
print(round(tr, 6))