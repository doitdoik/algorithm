# boj 16120 PPAP

s = input()
stack = []
ppap = ["P", "P", "A", "P"]

for i in range(len(s)):
    stack.append(s[i])
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")