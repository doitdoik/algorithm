n = int(input())
arr = list(input())
l = len(arr)

for i in range(n - 1):
    other = list(input())
    for j in range(l):
        if arr[j] != other[j]:
            arr[j] = '?'
            
print(''.join(arr))
    