import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(n):
    left, right = 0, n - 1
    target = arr[i]

    while left < right:
        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue
        
        if arr[left] + arr[right] == target:
            result += 1
            break

        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

print(result)