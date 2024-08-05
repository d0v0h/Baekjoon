def safe(node):
    for i in range(node):
        if (node-i == abs(graph[node] - graph[i])):
            return False
    return True

def sol(row):
    global ans
    if row == n:
        ans += 1
        return

    # n개의 열에 대해서 반복
    for i in range(n):          # (row, i) 방문
        if not visited[i]:      # (row, i) 방문 여부 확인
            graph[row] = i      # (row, i) 입력

            # backtracking 부분
            if safe(row):           # (row, i)의 퀸이 안전하다면
                visited[i] = True   # (row, i) 방문 체크
                sol(row+1)          # (row+1, i) 체크
                visited[i] = False 

n = int(input())

graph = [0] * n
visited = [False] * n
ans = 0

sol(0)
print(ans)