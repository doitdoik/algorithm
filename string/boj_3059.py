# boj 3059 등장하지 않는 문자의 합
t = int(input())

for _ in range(t):
    l = [i for i in range(65, 91)]
    for i in input():
        l[ord(i)-65] = 0
    print(sum(l))
