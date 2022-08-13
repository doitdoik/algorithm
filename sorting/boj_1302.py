n = int(input())
books = {}
for _ in range(n) :
    name = input()
    if name in books :
        books[name] += 1
    else :
        books[name] = 1

res = []
for j in books :
    res.append((j, books[j]))

res.sort(key=lambda x:(-int(x[1]), x[0]))

print(res[0][0])