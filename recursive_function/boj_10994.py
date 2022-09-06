n = int(input())
star = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]

def draw_star(n, x, y):
    if n == 1:
        star[y][x] = '*'
        return
    
    length = 4 * n -3

    for i in range(length):
        star[y][x+i] = '*'
        star[y+i][x] = '*'
        star[y+length-1][x+i] = '*'
        star[y+i][x+length-1] = '*'
    
    draw_star(n-1, x+2, y+2)

draw_star(n, 0, 0)

for j in star:
    print(''.join(j))