import sys

input = sys.stdin.readline
l, p, v = map(int, input().split())
case = 0

while (True):
    if (l==0) and (p==0) and (v==0):
        break
    case += 1
    res = 0
    res = (v//p)*l+min(v%p,l)

    print("Case ",case,": ",res, sep='')

    l,p,v = map(int, input().split())