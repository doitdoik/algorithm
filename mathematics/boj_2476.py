# boj 2476 주사위 게임
n = int(input())
money = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if a == b == c :
        money = max(money, 10000+a*1000)
    elif a == b:
        money = max(money, 1000+a*100)
    elif a == c:
        money = max(money, 1000+a*100)
    elif b == c:
        money = max(money, 1000+b*100)
    else :
        money = max(money, max(a,b,c)*100)
        
print(money)