import sys; input = sys.stdin.readline

# 행 확인
def check_row(row, num):
    for y in range(9):
        if num == graph[row][y]:
            return False
    return True

# 열 확인
def check_col(col, num):
    for x in range(9):
        if num == graph[x][col]:
            return False
    return True

# 3x3 영역 확인
def check_3by3(row, col, num):
    rs = (row // 3) * 3
    cs = (col // 3) * 3
    for x in range(3):
        for y in range(3):
            if num == graph[rs + x][cs + y]:
                return False
    return True

# 스토쿠 채우기
def dfs(depth):
    # depth: 호출 횟수
    if depth == len(empty_cell):
        for item in graph:
            print(*item, sep='')
        exit()
    
    x, y = empty_cell[depth]
    for num in range(1, 10):
        if check_row(x, num) and check_col(y, num) and check_3by3(x, y, num):
            graph[x][y] = num
            dfs(depth + 1)
            graph[x][y] = 0


# 스토쿠 입력
graph = []
empty_cell = []
for i in range(9):
    temp = list(map(int, input().strip()))
    graph.append(temp)
    for j in range(9):
        if graph[i][j] == 0:
            empty_cell.append((i, j))

dfs(0)