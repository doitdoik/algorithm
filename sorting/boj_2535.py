# boj 2535 아시아 정보올림피아드
n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
nums = sorted(nums, key = lambda x : x[2], reverse=True)
cnt = [0] * (n+1)
res = 0
i = 0
while res < 3:
    if cnt[nums[i][0]] < 2:
        cnt[nums[i][0]] += 1
        print(nums[i][0],nums[i][1])
        res += 1
    i += 1