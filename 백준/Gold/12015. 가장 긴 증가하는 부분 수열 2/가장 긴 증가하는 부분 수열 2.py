import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = []

for item in arr:
    left, right = 0, len(lis) - 1

    # item이 lis에 위치해야하는 인덱스 이분탐색
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    
    if left == len(lis):
        lis.append(item)
    else:
        lis[left] = item

print(len(lis))