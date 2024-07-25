import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

min_height = 257
max_height = -1
min_time = 1e9
good_height = -1

# 땅의 최소, 최대 높이를 계산 (필요한 블럭을 계산하기 위해서)
for item in arr:
    max_item = max(item)
    min_item = min(item)

    if max_height < max_item:
        max_height = max_item
    if min_height > min_item:
        min_height = min_item

# 가능한 모든 높이에서 시간 계산
for optimal_height in range(min_height, max_height+1):
    take_block = 0
    sub_block = 0

    # 일정 높이에서 필요한 블럭 개수 계산
    for item in arr:
        for height in item:
            if height < optimal_height:
                take_block += optimal_height - height
            else:
                sub_block += height - optimal_height
    
    # 블럭 개수를 통해서 소요 시간 계산
    if take_block <= sub_block + b:
        total_time = take_block + 2 * sub_block
        if total_time <= min_time and optimal_height > good_height:
            min_time = total_time
            good_height = optimal_height

print(min_time, good_height)