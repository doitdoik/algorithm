words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

res = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            res += words[j][i]

print(res)