import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []
    # 무방향 그래프 케이스
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
        graph.append((b, a, c))
    # 웜홀 케이스
    for _ in range(w):
        a, b, c = map(int, input().split())
        graph.append((a, b, -c))
    
    def dijkstra(node):
        dist = [1e9] * (n+1)
        dist[node] = 0

        # n-1번 거리 값 계산
        for i in range(n):
            # 최소 거리 갱신
            for start, end, cost in graph:
                if dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost
                    # n-1번째에도 거리 갱신이 존재하면 음수 사이클 존재
                    if i == n-1:
                        return 'YES'
        return 'NO'
    print(dijkstra(1))