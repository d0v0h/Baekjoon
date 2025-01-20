import sys; input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
arr_sum = 0
result = float('inf')

while right < n:
    arr_sum += arr[right]

    while arr_sum >= target:
        result = min(result, right - left + 1)
        arr_sum -= arr[left]
        left += 1
    right += 1

if result == float('inf'):
    print(0)
else:
    print(result)