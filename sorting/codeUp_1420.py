n = int(input())
record = {}

for _ in range(0, n):
    name, score = input().split()
    record[name] = int(score)

data = sorted(record.items(), key=lambda x: x[1], reverse=True)

print(data[2][0])