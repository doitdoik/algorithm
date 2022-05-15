import sys
sys.setrecursionlimit(1000000)

res = 0
def func(n):
  global res
  if(n!=1):
    func(n-1)
  res += n
  
func(int(input()))
print(res)
