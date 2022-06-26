n = input()
f = int(input())
fix_n = int(n[:-2]+'00')

while True :
    if fix_n % f == 0 :
        break
    fix_n += 1

print(str(fix_n)[-2:])