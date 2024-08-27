def check_row(n, row):
    for j in range(9):
        if n == arr[row][j]:
            return False
    return True

def check_col(n, col):
    for i in range(9):
        if n == arr[i][col]:
            return False
    return True

def check_3by3(n, row, col):
    for i in range((row // 3 * 3), (row // 3 * 3 + 3)):
        for j in range((col // 3 * 3), (col // 3 * 3 + 3)):
            if arr[i][j] == n:
                return False
    return True

arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

# 0인 좌표를 empty 리스트에 저장하여 처리
empty = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty.append([i, j])

def btk(n):
    if n == len(empty):
        for r in arr:
            print(*r)
        exit(0)

    row = empty[n][0]
    col = empty[n][1]

    for i in range(1, 10):
        if check_row(i, row) and check_col(i, col) and check_3by3(i, row, col):
            arr[row][col] = i   # 스도쿠 조건에 충족되면 대입
            btk(n+1)            # 다음 빈칸 호출
            arr[row][col] = 0   # 이후 호출에서 아무것도 이루어지지 않으면 다음 경우의 수 계산

btk(0)