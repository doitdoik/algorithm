arr = list(input())
stack = []
tmp = 1
res = 0

for i in range(len(arr)) : 
  if arr[i] == '(' :
    tmp *= 2
    stack.append(arr[i])
  if arr[i] == '[' :
    tmp *= 3
    stack.append(arr[i])
  
  if arr[i] == ')' :
    if not stack or stack[-1] == '[' :
      res = 0
      break
    elif arr[i-1] == '(' :
      res += tmp
    tmp //= 2
    stack.pop()

  if arr[i] == ']' :
    if not stack or stack[-1] == '(' :
      res = 0
      break
    elif arr[i-1] == '[' :
      res += tmp
    tmp //= 3
    stack.pop()
    
if stack : 
  res = 0
  
print(res)