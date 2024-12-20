import sys; input = sys.stdin.readline

str = input().strip()
arr = list(str)
arr.sort(reverse=True)

print(*arr, sep='')