import sys; input = sys.stdin.readline

m, n, k = map(int, input().split())

arr = []
for _ in range(m):
    arr.append(input().strip())

w_index = [[0] * (n+1) for _ in range(m+1)]
b_index = [[0] * (n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):

        w_index[i+1][j+1] = w_index[i][j+1] + w_index[i+1][j] - w_index[i][j]
        b_index[i+1][j+1] = b_index[i][j+1] + b_index[i+1][j] - b_index[i][j]

        if (i + j) % 2 == 0:
            if arr[i][j] != 'W':
                w_index[i+1][j+1] += 1
            else:
                b_index[i+1][j+1] += 1
        else:
            if arr[i][j] != 'W':
                b_index[i+1][j+1] += 1
            else:
                w_index[i+1][j+1] += 1

min_result = float('inf')
for i in range(m - k + 1):
    for j in range(n - k + 1):
        min_w = w_index[i+k][j+k] - w_index[i+k][j] - w_index[i][j+k] + w_index[i][j] 
        min_b = b_index[i+k][j+k] - b_index[i+k][j] - b_index[i][j+k] + b_index[i][j]
        
        min_result = min(min_result, min_w, min_b)

print(min_result)