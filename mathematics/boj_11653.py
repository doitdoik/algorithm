# boj 11653 소인수분해

n = int(input())
while n-1:
    for i in range(2, int(n)+1):
        if n%i == 0:
            print(i)
            n = n/i
            break