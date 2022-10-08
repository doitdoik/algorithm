n = int(input())
cnt = [0 for _ in range(500001)]
nums = list(map(int, input().split()))

for i in range(n):
    num = nums[i]
    cnt[num] += 1

for i in range(len(cnt)-1):
    cnt[i+1] += cnt[i]

for i in nums:
    print(cnt[i]-1, end = ' ')