# boj 1037 약수

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0]*a[-1])