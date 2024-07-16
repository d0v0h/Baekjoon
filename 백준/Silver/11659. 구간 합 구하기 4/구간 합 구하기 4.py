import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sum_arr = [0]
arr = list(map(int, input().split()))

sum_item = 0
for item in arr:
    sum_item += item
    sum_arr.append(sum_item)

for _ in range(m):
    a, b = map(int, input().split())

    result = sum_arr[b] - sum_arr[a-1]
    print(result)