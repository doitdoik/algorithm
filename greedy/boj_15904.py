n = input()
ucpc = ['U', 'C', 'P', 'C']
res = ""
cnt = 0

for i in n :
    if res == "UCPC" : break 
    elif i.isupper() and i == ucpc[cnt] : 
        res += i 
        cnt += 1

if res == "UCPC" : 
    print("I love UCPC")
else : 
    print("I hate UCPC")