x, y = map(str, input().split())
x = int(x[::-1]) 
y = int(y[::-1]) 
res = str(x + y)

print(int(res[::-1]))