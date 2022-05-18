def fibonacci(n):
  if n == 0 or n == 1:
    return n
  if l[n] == 0:
    l[n] = fibonacci(n-1) + fibonacci(n-2)
  return l[n]
  
N = int(input())
l = [0]*201
print(fibonacci(N)%10009)