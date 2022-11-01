import sys

input = sys.stdin.readline
n = int(input())
ex = input().rstrip()
stack = []
nums = []

for i in range(n):
    nums.append(input().rstrip())

for s in ex:
    if s not in ['+','-','*','/']:
        stack.append(nums[ord(s)-ord('A')])
    else:
        a2 = stack.pop()
        a1 = stack.pop()
        stack.append(str(eval(a1 + s + a2)))

print('%.2f' %(float(stack[0])))