arr = [] 

for i in range(5): 
    w = input() 
    if "FBI" in w: 
        arr.append(i+1) 
if arr: 
    print(*arr) 
else: 
    print("HE GOT AWAY!")