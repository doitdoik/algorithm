# boj 5596 시험 점수
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
t = sum(b)
print(max(s, t))