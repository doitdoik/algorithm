# boj 10039 평균 점수

total = 0
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    total += n
avg = total//5
print(avg)