import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
k = int(input())

if k == 1:
    for i in graph:
        print(*i, sep='')

elif k == 2:
    for i in graph:
        i.reverse()
        print(*i, sep='')

elif k == 3:
    graph.reverse()
    for i in graph:
        print(*i, sep='')
