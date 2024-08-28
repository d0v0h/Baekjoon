import sys; input = sys.stdin.readline

n = int(input())

img = []
for _ in range(n):
    img.append(list(map(int, input().split())))

result = [0, 0, 0] # -1, 0, 1의 개수 count
def dnc(n, row, col):
    check = img[row][col]
    is_same = True
    for i in range(row, row+n):
        for j in range(col, col+n):
            if check != img[i][j]:
                is_same = False
                break

    if is_same:
        result[check+1] += 1
    
    else:
        for i in range(3):
            for j in range(3):
                dnc(n//3, row+(n//3)*i, col+(n//3)*j)

dnc(n, 0, 0)
print(*result, sep='\n')