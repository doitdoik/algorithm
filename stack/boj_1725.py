import sys

input=sys.stdin.readline
n = int(input())
graph = []
res = 0
cursor = 0
a = 0

for _ in range(n):
  graph.append(int(input()))

graph.append(0)
stack = [(0, graph[0])]

for i in range(1,n+1):
  cursor = i
  while stack and stack[-1][1] > graph[i]:
      cursor, temp = stack.pop()
      res = max(res, temp*(i-cursor))
  stack.append((cursor, graph[i]))
  
print(res)
  