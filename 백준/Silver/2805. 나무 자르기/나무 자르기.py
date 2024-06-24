import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for t in tree:
        if t > mid:
            total += t - mid
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)