import sys

input = sys.stdin.readline
n = 0
while True:
    stack = []
    k = 0
    n += 1
    s = input()

    if '-' in s:
        break
    for i in s:
        if i == '{':
            stack.append(i)
        elif i == '}' and stack:
            stack.pop()
        elif i == '}' and not stack:
            stack.append('{')
            k += 1
    if len(stack) != 0:
        k += len(stack)//2

    print(f"{n}. {k}")