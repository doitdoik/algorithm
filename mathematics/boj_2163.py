# boj 2163 초콜릿 자르기
n, m = map(int, input().split())
row = n-1
col = m-1

res = n * col
print(row + res)