# boj 5586 JOI와 IOI
s = input()
JOI = 0
IOI = 0

for i in range(len(s)-2):
    res = ''
    res += s[i] + s[i+1] + s[i+2] 
    
    if res == 'JOI':
        JOI += 1
    if res == 'IOI':
        IOI += 1
        
print(JOI)
print(IOI)