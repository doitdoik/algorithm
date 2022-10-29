import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
students = deque()
check = [0]*21
cnt = 0

for _ in range(n):
    if len(students) == k+1:
        check[len(students[0])] -= 1
        students.popleft()

    person = input().strip()
    num = len(person)
    cnt += check[num]
    check[num] += 1    
    students.append(person)

print(cnt)