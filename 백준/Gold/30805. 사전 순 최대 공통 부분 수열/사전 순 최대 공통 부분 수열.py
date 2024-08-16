from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

result = []
while len(A) and len(B):

    max_A, max_B = max(A), max(B)

    # 최대값이 같아지면 나중 수열을 구할 수 있음.
    if max_A == max_B:
        result.append(max_A)
        A = A[A.index(max_A)+1:]
        B = B[B.index(max_B)+1:]
    
    elif max_A > max_B:
        A.remove(max_A)
    
    else:
        B.remove(max_B)

print(len(result))
print(*result)