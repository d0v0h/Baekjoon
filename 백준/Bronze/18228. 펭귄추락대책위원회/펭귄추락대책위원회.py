import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

idx = arr.index(-1)
left_min = min(arr[:idx])
right_min = min(arr[idx+1:])

print(left_min + right_min)