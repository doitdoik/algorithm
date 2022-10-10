k = int(input())

for i in range(k):
    student = list(map(int, input().split()))
    del student[0]
    student.sort()
    diff = []

    print('Class', i+1)
    
    for i in range(len(student)-1):
        diff.append(student[i+1] - student[i])

    print('Max', str(max(student))+',' ,'Min', str(min(student))+',', 'Largest gap', max(diff))