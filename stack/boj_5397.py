import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    password = list(input().strip())
    l_stack = []
    r_stack = []

    for j in password:
        if j == '<':
            if l_stack:  
                r_stack.append(l_stack.pop())
        elif j == '>':
            if r_stack:  
                l_stack.append(r_stack.pop())
        elif j == '-':
            if l_stack:  
                l_stack.pop()
        else:
            l_stack.append(j)

    l_stack.extend(reversed(r_stack))

    print(''.join(l_stack))