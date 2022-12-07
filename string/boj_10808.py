s = str(input())  # baekjoon
alphabet = {chr(x):0 for x in range(97, 123)}

for i in s:
    if i in alphabet:
        alphabet[i] = alphabet[i] +1

for x in alphabet:
    print(alphabet[x], end=' ')

    