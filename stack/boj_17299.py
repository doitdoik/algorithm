import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 1000001

    for i in arr:
        cnt[i] += 1

    stack = []
    res = [-1] * n
    
    for i in range(n):
        while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
            res[stack.pop()] = arr[i]
        stack.append(i)

    print(' '.join(map(str, res)))

main()