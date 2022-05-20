def wubak(n) :
    print(n)
    
    if n==1 :
        return 1

    if n%2==1 :
        return wubak(3*n+1)
    else :
        return wubak(n//2)

N = int(input())

wubak(N)