import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = float('inf')

answer = []
for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        temp_sum = arr[left] + arr[i] + arr[right]
        if abs(temp_sum) < result:
            result = abs(temp_sum)
            answer = [arr[i], arr[left], arr[right]]
        
        if temp_sum < 0:
            left += 1
        elif temp_sum > 0:
            right -= 1
        else:
            print(*answer)
            exit(0)

print(*answer)