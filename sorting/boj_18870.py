import sys

input = sys.stdin.readline
n = int(input())
x_list = list(map(int, input().split()))
set_x = list(sorted(set(x_list)))

dic = {set_x[i]: i for i in range(len(set_x))}

for j in x_list:
    print(dic[j], end = ' ')
