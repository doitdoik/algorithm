# boj 14729 칠무해
import sys

input = sys.stdin.readline
n = int(input())
l = [float(input()) for _ in range(n)]

l.sort() 
for i in range(7):
  print('%.3f' %l[i])