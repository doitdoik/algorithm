# boj 3460 이진수

t = int(input())
    
for _ in range(t):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')