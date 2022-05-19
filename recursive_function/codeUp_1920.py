def binary(n):
    global res
    if n // 2 == 1:
        res.append(n//2)
        res.append(n % 2)
    elif n // 2 == 0:
        res.append(n % 2)
    else:
        binary(n // 2)
        res.append(n % 2)
    return ''.join(map(str,res))
N = int(input())
res= []
print(binary(N))