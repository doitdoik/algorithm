import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boards = [input() for _ in range(n)]
res = 64
for i in range(n-7) : 
    for j in range(m-7) :
        w_cnt = 0
        b_cnt = 0
        for k in range(i, i+8) : 
            for l in range(j, j+8) :
                if (k+l)%2 == 0 :
                    if boards[k][l] != 'B' : 
                        b_cnt += 1 
                    if boards[k][l] != 'W' :
                        w_cnt += 1
                else : 
                    if boards[k][l] != 'B' :
                        w_cnt += 1
                    if boards[k][l] != 'W' :
                        b_cnt += 1
        res = min(res, w_cnt, b_cnt)

print(res)