n = int(input())

def matmul(matrix_1, matrix_2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j] % 1000000007
    
    return result

matrix = [[1, 1], [1, 0]]
def sol(n, matrix):
    if n == 0:
        return [[0, 0], [0, 0]]
    elif n == 1:
        return matrix
    else:
        temp = sol(n//2, matrix)
        if n % 2 == 0:
            return matmul(temp, temp)
        else:
            return matmul(matmul(temp, temp), matrix)

print(sol(n, matrix)[0][1] % 1000000007)