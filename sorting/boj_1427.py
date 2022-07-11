n = input()
arr = []
for i in range(len(n)) :
    arr.append(int(n[i]))

arr.sort(reverse=True)

for j in arr :
    print(j, end='')

