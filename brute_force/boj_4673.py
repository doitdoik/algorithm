def self_number(num):
    self_num = num
    while num != 0:
        self_num += num%10
        num //= 10
    return self_num
        
res = set()

for i in list(range(1,10001)):
    if i not in res:
        print(i)
    res.add(self_number(i))