
def factorial(a):
    if a==1:
        return 1
    return a*factorial(a-1)

n = int(input())

factorial(n)

print(factorial(n))