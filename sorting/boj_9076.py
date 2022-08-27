t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))
    n.sort()
    
    if abs(n[1]-n[3]) >= 4:
        print("KIN")
    else:
        print(sum(n)-max(n)-min(n))