import sys
input = sys.stdin.readline

n, b = map(int, input().split())

matrix = []
mod = [1000 for _ in range(n)]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 행렬 곱
def calc(matrix_1, matrix_2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j] % 1000
    return result

# 1629 곱셈 코드 응용하여 해결 (분할 정복을 통해 n^3 log b의 시간복잡도를 가짐)
def modulo(mat, b):
    if b == 1:
        return mat
    else:
        result = modulo(mat, b//2)
        if b % 2 == 0:
            return calc(result, result)
        else:
            return calc(calc(result, result), mat)

answer = modulo(matrix, b)

for a in answer:
    for i in range(len(a)):
        print(a[i] % 1000, end=' ')
    print()