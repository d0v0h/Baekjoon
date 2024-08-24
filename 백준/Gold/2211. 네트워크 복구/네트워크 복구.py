import sys, heapq; input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(node):
    queue = []
    heapq.heappush(queue, (0, node))

    cost = [1e9] * (n+1)
    prev = [-1] * (n+1)
    cost[node] = 0

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_cost > cost[cur_node]:
            continue

        for next_cost, next_node in graph[cur_node]:
            total_cost = cur_cost + next_cost
            if cost[next_node] > total_cost:
                cost[next_node] = total_cost
                prev[next_node] = cur_node
                heapq.heappush(queue, (total_cost, next_node))
        
    return prev

edge = dijkstra(1)

result = []
for i in range(2, n+1):
    result.append((edge[i], i))

print(len(result))
for a, b in result:
    print(a, b)