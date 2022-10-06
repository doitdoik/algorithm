import sys

input = sys.stdin.readline
n = int(input())
nums = []

for _ in range(0, n):
    number = int(input())
    nums.append(number)
    
nums.sort()

print(*nums)