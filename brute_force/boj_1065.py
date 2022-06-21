n = int(input())

def hansu(num) :
    res = 0
    for i in range(1, num+1) :
        numlist = list(map(int, str(i)))
        if i < 100 : 
            res += 1
        else : 
            if numlist[0] - numlist[1] == numlist[1] - numlist[2] : 
                res += 1
    print(res)

hansu(n)
