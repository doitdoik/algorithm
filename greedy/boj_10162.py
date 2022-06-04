T = int(input())
R = T % 300

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = R // 60
    C = R % 60 // 10
    print(A, B, C)