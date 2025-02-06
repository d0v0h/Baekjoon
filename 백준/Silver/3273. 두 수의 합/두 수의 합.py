import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

left = 0; right = n-1; result = 0
while left < right:
    temp_sum = arr[left] + arr[right]
    if temp_sum > x:
        right -= 1
    elif temp_sum < x:
        left += 1
    else:
        result += 1
        left += 1
print(result)