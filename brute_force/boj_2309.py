dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
total = sum(dwarf)

for i in range(len(dwarf)) :
    for j in range(i+1,len(dwarf)) :
        if (total - dwarf[i] - dwarf[j]) == 100 :
            tmp1 = dwarf[i]
            tmp2 = dwarf[j]

dwarf.remove(tmp1)
dwarf.remove(tmp2)

print('\n'.join(map(str, dwarf)))