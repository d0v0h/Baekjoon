import sys; input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    cmd = list(map(int, input().split()))
    graph[cmd[0]].append(cmd[1])
    graph[cmd[1]].append(cmd[0])

k = int(input())
bomb = list(map(int, input().split()))

result = []
total_bomb = []
for b in bomb:
    check = [b]
    for destroyed_city in graph[b]:
        if destroyed_city not in bomb:
            break
        check.append(destroyed_city)
    else:
        result.append(b)
        total_bomb.extend(check)

for check in bomb:
    if check not in total_bomb:
        print(-1)
        exit()
print(len(result))
print(*result)