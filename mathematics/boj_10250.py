# boj 10250 ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    a = 0 
    b = 0

    if n%h == 0:
        a = h*100
        b = n//h
    else:
        a = (n%h)*100
        b = n//h + 1

    print(a + b)