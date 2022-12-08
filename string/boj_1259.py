import sys

while True:
    input = sys.stdin.readline
    s = input().rstrip()

    if s == s[::-1] and s != '0':
        print('yes')
    elif s == '0':
        sys.exit()
    else:
        print('no')    