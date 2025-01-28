from itertools import combinations
from bisect import bisect_left, bisect_right
import sys; input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 절반으로 나눠서 계산
left_arr = arr[:n//2]
right_arr = arr[n//2:]

# 왼쪽 배열에서 부분 수열 합 계산
left_sum = []
for i in range(1, len(left_arr)+1):
    for com in combinations(left_arr, i):
        left_sum.append(sum(com))

# 오른쪽 배열에서 부분 수열 합 계산
right_sum = []
for i in range(1, len(right_arr)+1):
    for com in combinations(right_arr, i):
        right_sum.append(sum(com))
right_sum.sort()

# 왼쪽 부분 수열 합에 대해 오른쪽 부분수열의 합과 s가 되는 부분 탐색
result = 0
for item in left_sum:
    result += bisect_right(right_sum, s - item) - bisect_left(right_sum, s - item)

# 각 부분 수열 스스로 합이 s가 되는 부분
result += left_sum.count(s)
result += right_sum.count(s)

print(result)