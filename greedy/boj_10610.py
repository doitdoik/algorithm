n = list(input())
n.sort(reverse=True)
nSum = 0

for i in n :
    nSum += int(i)

if nSum % 3 == 0 and '0' in n :
    print(''.join(n))
else : 
    print(-1)