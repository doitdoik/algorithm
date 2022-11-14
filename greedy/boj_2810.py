n = int(input())
data = input()
cnt = 0

for i in range(len(data)):
  if data[i] == 'L':  
    cnt += 1
 
if cnt == 0: 
  print(n)
else:
  print(n-(cnt//2-1))