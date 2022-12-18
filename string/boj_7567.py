bowl = list(input())
height = 10

n=len(bowl)

for i in range(len(bowl)):
    if bowl[i] == bowl[i+1]:
        height += 5
    else :
        height += 10 

print(height)