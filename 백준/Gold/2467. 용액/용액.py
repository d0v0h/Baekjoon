import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [float('inf'), 0, 0]

for i in range(n-1):
    now = arr[i]
    left = i + 1
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        temp = now + arr[mid]

        if abs(temp) < result[0]:
            result[0] = abs(temp)
            result[1] = i
            result[2] = mid
            
        if temp < 0:
            left = mid + 1
        else:
            right = mid - 1

print(arr[result[1]], arr[result[2]])