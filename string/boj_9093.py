import sys

input =  sys.stdin.readline
n = int(input())
 
for _ in range(n):
  words = input().rstrip().split()
 
  for i in words:
    print(i[::-1], end=' ')

  print()