# boj 10886 0 = not cute / 1 = cute
n = int(input())
cnt = 0

for _ in range(n):
    if int(input()) == 1:
        cnt += 1

if cnt > n//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")