import sys, heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    max_heap = []
    min_heap = []
    visited = [False] * k   # 동기화를 위해 visited 작성
    for i in range(k):
        cmd, num = input().split()
        if cmd == 'I':
            heapq.heappush(max_heap, (-int(num), i))
            heapq.heappush(min_heap, (int(num), i))
            visited[i] = False

        elif cmd == 'D':
            if int(num) == -1:
                while min_heap and visited[min_heap[0][1]]:     # max_heap에서 이미 원소가 삭제된 경우
                    heapq.heappop(min_heap)                     # 동기화 수행
                if min_heap:
                    visited[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            else:
                while max_heap and visited[max_heap[0][1]]:     # min_heap에서 이미 원소가 삭제된 경우
                    heapq.heappop(max_heap)                     # 동기화 수행
                if max_heap:
                    visited[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
    
    # 마지막 동기화
    while min_heap and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # t번째 테스트 케이스에 해당하는 값 출력
    if min_heap or max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')