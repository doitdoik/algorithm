# boj 1296 팀 이름 정하기
import sys

input = sys.stdin.readline
name = input().rstrip()
n = int(input().rstrip())
arr = []
for i in range(n):
    teamName = input().rstrip()
    s = name+teamName
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    num = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    arr.append((num, teamName))
    
arr.sort(key=lambda x : (-x[0], x[1]))

print(arr[0][1])