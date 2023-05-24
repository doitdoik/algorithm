# boj 2407 조합
import math

n, m = map(int, input().split())
numer = math.factorial(n)
deno = (math.factorial(n-m)) * (math.factorial(m))

print(numer//deno)