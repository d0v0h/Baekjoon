import sys; input = sys.stdin.readline

arr = [0 for _ in range(5)]

for idx in range(1, 5):
    o, i = map(int, input().split())
    arr[idx] = arr[idx-1] + (i - o)

print(max(arr))