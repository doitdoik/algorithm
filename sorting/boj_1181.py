import sys

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n) : 
    word = input().strip()
    cnt = len(word)
    arr.append((cnt, word))

set_arr = list(set(arr))

set_arr.sort(key = lambda words : (words[0], words[1]))

for i in set_arr :
    print(i[1])
