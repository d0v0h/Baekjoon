from itertools import combinations, permutations
import sys; input = sys.stdin.readline

N = int(input())
graph = []
comb_arr = [i for i in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

MIN = 1e9
for start in combinations(comb_arr, N//2):
    s, l = 0, 0
    link = []
    for i in range(N):
        if i not in start:
            link.append(i)


    for perm in permutations(start, 2):
        s += graph[perm[0]][perm[1]]
    
    for perm in permutations(link, 2):
        l += graph[perm[0]][perm[1]]

    MIN = min(MIN, abs(s - l))

print(MIN)