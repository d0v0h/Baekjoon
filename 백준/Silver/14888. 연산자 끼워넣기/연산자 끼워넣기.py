N = int(input())
A = list(map(int, input().split()))
opr = list(map(int, input().split()))

MIN = int(1e9)
MAX = int(-1e9)

def btk(n, arr):
    global MAX, MIN
    if n == N-1:
        MAX = max(MAX, arr)
        MIN = min(MIN, arr)
        return
    
    if opr[0] != 0:
        opr[0] -= 1
        btk(n+1, arr + A[n+1])
        opr[0] += 1

    if opr[1] != 0:
        opr[1] -= 1
        btk(n+1, arr - A[n+1])
        opr[1] += 1

    if opr[2] != 0:
        opr[2] -= 1
        btk(n+1, arr * A[n+1])
        opr[2] += 1

    if opr[3] != 0:
        opr[3] -= 1
        if arr > 0:
            btk(n+1, arr // A[n+1])
        else:
            btk(n+1, -(-arr // A[n+1]))
        opr[3] += 1

    
btk(0, A[0])
print(MAX)
print(MIN)