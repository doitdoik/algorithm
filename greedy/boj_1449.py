N, L = map(int, input().split())
hole = list(map(int, input().split()))

hole.sort()

start = hole[0]
end = hole[0] + L
cnt = 1

for i in range(N) : 
    if start <= hole[i] < end :
        continue
    else :
        start = hole[i]
        end = hole[i] + L
        cnt += 1

print(cnt)