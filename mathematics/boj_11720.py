# boj 11720 숫자의 합

n = int(input())
s = input()
res = 0

for i in range(len(s)):
    res += int(s[i])

print(res)