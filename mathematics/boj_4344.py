# boj 4344 평균은 넘겠지

c = int(input())

for i in range(c):
    cnt = 0 
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    for j in arr[1:]:
        if j > avg:
            cnt += 1
    print(f'{cnt/arr[0]*100:.3f}%')