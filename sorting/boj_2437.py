n=int(input())
weight=list(map(int, input().split()))
weight.sort()
res=1

for i in weight:
    if res < i:
        break
    res += i
print(res)