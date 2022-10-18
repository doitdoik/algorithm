texts = input()
bomb = list(input())
stack = list()

for i in texts:
    stack.append(i)
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))