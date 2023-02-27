# boj 4153 직각삼각형

res = []
 
while True:
    tri = list(map(int, input().split()))
 
    if sum(tri) == 0:
        break
 
    maximum = max(tri)
    tri.remove(maximum)
 
    if ((maximum ** 2) == (tri[0] ** 2) + (tri[1] ** 2)):
        res.append('right')
    else:
        res.append('wrong')
 
for i in range(0, len(res)):
    print(res[i])