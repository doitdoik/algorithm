n = int(input())
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split())))

arr.sort(key= lambda xy : (xy[1], xy[0]))

for i in arr :
    print(i[0], i[1])