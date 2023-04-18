# boj 2910 빈도 정렬

n, c = map(int, input().split())
seq = list(map(int, input().split()))
cnt = {}
idx = 1
for s in seq:
    if s in cnt:
        cnt[s][0] +=1
    else:
        cnt[s] = [1, idx]
        idx += 1
        
nums = [[i, j] for i, j in cnt.items()]
nums.sort(key=lambda x:(-x[1][0], x[1][1]))
res = []
for i, j in nums:
    res += [i]*j[0]
    
print(*res)