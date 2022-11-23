n, m = map(int, input().split())
j = int(input())
apple = []
 
for _ in range(j):
    apple.append(int(input()))
 
res = 0
end = m     
start = 1   
 
for i in range(j):
    if(end >= apple[i] and start <= apple[i]):
        continue
    elif (end < apple[i]):
        res += apple[i] - end
        end = apple[i]
        start = apple[i] - (m - 1)
    elif (start > apple[i]):
        res += start - apple[i]
        start = apple[i]
        end = apple[i] + (m - 1)
 
print(res)