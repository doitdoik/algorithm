s = input()
alph=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    s = s.replace(i, '*')
    
print(len(s))