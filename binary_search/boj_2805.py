import sys

input = sys.stdin.readline
n , m = map(int, input().split())
tree = list(map(int, input().split()))

def cut_tree(arr, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for x in arr:
            if x > mid:
                total += x - mid
            
        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    return res

print(cut_tree(tree, 0, max(tree)))