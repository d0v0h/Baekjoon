import sys; input = sys.stdin.readline

n, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

# 공유기 최소, 최대 거리
left, right = 1, arr[-1] - arr[0]
result = 0

while left <= right:
    mid = (left + right) // 2   # 최대 최소 거리의 중간거리 기준으로 계산
    current = arr[0]
    router = 1

    # 최대 거리에 공유기 설치
    for i in range(1, n):
        if arr[i] - current >= mid:
            router += 1
            current = arr[i]
    
    if router < c:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)