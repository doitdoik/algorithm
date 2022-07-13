from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))

# 평균
print(round(sum(arr)/n))

# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값 : 가장 자주 나온 숫자. 데이터에서 가장 많이 등장한 숫자 # collections - Counter 사용
arr_mode = Counter(arr).most_common()

if len(arr_mode) > 1 :
    if arr_mode[0][1] == arr_mode[1][1] :
        print(arr_mode[1][0])
    else : 
        print(arr_mode[0][0])
else : 
    print(arr_mode[0][0])

# 범위
print(arr[-1] - arr[0])
