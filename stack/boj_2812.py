n, k = map(int, input().split())
num = list(input())
cnt = k
stack = []

for i in range(n):
    while cnt and stack:
        if stack[-1] < num[i]:
            stack.pop()
            cnt -= 1
        else:
            break
    stack.append(num[i])

print(''.join(stack[:n-k]))