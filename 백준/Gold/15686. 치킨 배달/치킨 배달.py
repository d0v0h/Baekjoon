from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 좌표 저장
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))

# 가정집 좌표 저장
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i,j))

# 치킨집과 가정집 사이의 거리 계산
def cal_distance(chickens):
    distance = 0
    for house in houses:
        h_x, h_y = house
        min_dist = 1e9
        for chicken in chickens:
            c_x, c_y = chicken
            dist = abs(c_x - h_x) + abs(c_y - h_y)
            min_dist = min(min_dist, dist)
        distance += min_dist
    return distance

# m개의 조합으로 치킨집과 가정집 사이의 거리 계산
min_dist = 1e9
for chicken in combinations(chickens, m):
    result = cal_distance(chicken)
    min_dist = min(min_dist, result)

print(min_dist)