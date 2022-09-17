import sys

input = sys.stdin.readline 
s = input().rstrip()
stack = []
cnt = 0
 
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
 
    else:   
        if s[i-1] == '(':   
            stack.pop()
            cnt += len(stack)
 
        else:    
            cnt += 1
            stack.pop()

print(cnt)