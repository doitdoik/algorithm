def wubak(n) :
    
    if n==1 :
        return print(1)

    if n%2==1 :
        wubak(3*n+1)
    else :
        wubak(n//2)
    return print(n)

N = int(input())

wubak(N)