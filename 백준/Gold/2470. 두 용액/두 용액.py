import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = float('inf')
answer = []

left = 0; right = n - 1
while left < right:
    if abs(arr[left] + arr[right]) < abs(result):
        result = arr[left] + arr[right]
        answer = [arr[left], arr[right]]
    
    if arr[left] + arr[right] > 0:
        right -= 1
    else:
        left += 1
        
answer.sort()
print(*answer)