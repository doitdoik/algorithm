def modify(string, cnt) :
    if len(string) > 1 :
        cnt += 1
        total = 0
        for i in string :
            total += int(i)
        modify(str(total), cnt)
    else : 
        if int(string) % 3 == 0 :
            print(cnt)
            print('YES')
        else : 
            print(cnt)
            print('NO')

n = input()
cnt = 0

modify(n, cnt)