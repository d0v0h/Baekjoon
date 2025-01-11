n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:k])
result = window

for i in range(n - k):
    window += (arr[i + k] - arr[i])
    result = max(result, window)

print(result)