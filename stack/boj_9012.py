import sys

input = sys.stdin.readline
t = int(input())

def check(stack):
    cnt = 0
    while stack:
        vps = stack.pop()
        if vps == ')':
            cnt += 1
        else:
            if cnt <= 0:
                return False
            cnt -= 1
    if cnt != 0:
        return False
    return True

for _ in range(t):
    stack = list(input().rstrip())
    if check(stack):
        print('YES')
    else:
        print('NO')