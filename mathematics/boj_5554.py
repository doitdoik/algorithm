# boj 5554 심부름 가는 길

res = 0

for i in range(4):
	res += int(input())
print(res // 60)
print(res % 60)