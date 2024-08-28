import sys; input = sys.stdin.readline

n = int(input())

img = []
for _ in range(n):
    img.append((input().strip()))

def sol(n, row, col):
    check = img[row][col]
    is_same = True
    for i in range(row, row+n):
        for j in range(col, col+n):
            if check != img[i][j]:
                is_same = False
                break
    
    if is_same:
        print(img[row][col], end='')
    
    else:
        print('(', end='')
        sol(n//2, row, col)
        sol(n//2, row, col+(n//2))
        sol(n//2, row+(n//2), col)
        sol(n//2, row+(n//2), col+(n//2))
        print(')', end='')

sol(n, 0, 0)