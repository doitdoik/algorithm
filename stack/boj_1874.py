import sys

input = sys.stdin.readline
n = int(input())
num_list = [int(input()) for _ in range(n)]
 
stack = [] 
res = [] 
no_res = True 
cnt = 0
 
for i in num_list:
    
    while cnt < i:
        cnt += 1
        stack.append(cnt)
        res.append('+')
        
    if stack[-1] == i:
        stack.pop()
        res.append('-')
    else:
        no_res = False
        break
    
if no_res == False:
    print('NO')
else:
    print('\n'.join(res))