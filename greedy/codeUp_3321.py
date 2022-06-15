n = int(input())
a, b = map(int, input().split())

c = int(input())
tp_list = []
for i in range(n) :
    tp_list.append(int(input()))

tp_list.sort(reverse=True)

res = 0 
price = 0
cal = 0

for i in tp_list :
    cal += i
    price += b
    tmp=(c+cal)/float(a+price)

    if res>tmp:
        break
    else:
        res=tmp

print(int(res))

