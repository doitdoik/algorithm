# boj 2204 도비의 난독증 테스트

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        s = input().rstrip()
        arr.append([s.lower(), s])
    arr.sort()
    print(arr[0][1])