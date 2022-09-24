import sys

input = sys.stdin.readline
n = int(input())
words = [list(input().rstrip()) for _ in range(n)]
cnt = 0
for i in words:
    stack = []
    while i:
        word = i.pop()
        if not stack:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
                
    if not stack:
        cnt += 1
print(cnt)