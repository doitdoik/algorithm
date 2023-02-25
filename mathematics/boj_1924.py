# boj 1924 2007년

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum = 0 
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
x, y = map(int,input().split())

for i in range(1, x): 
    if i in a :
        sum += 31
    elif i in b :
        sum += 30
    elif i == 2 :
        sum += 28  
    
sum += y
print(week[sum%7])