# boj 1193 분수찾기

x = int(input())
i = 1
while(True):
  if (x-i > 0):
    x -= i
    i += 1
  else:
    break
if (i+1)%2 == 1:
  print(f'{x}/{i-(x-1)}')
else:
  print(f'{i-(x-1)}/{x}')