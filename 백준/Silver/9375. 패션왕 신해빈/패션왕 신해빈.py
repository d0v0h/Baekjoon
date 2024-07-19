import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    wear = {}
    fashion = int(input())
    for _ in range(fashion):
        colthes, category = input().split()
        if category not in wear.keys():
            wear[category] = ['', colthes]  # 옷이 없는 경우와 옷이 있는 경우를 추가
        else:
            wear[category].append(colthes)  # 카테고리가 있으면 append
    
    result = 1
    for cnt in wear.keys():
        result *= len(wear[cnt])
    print(result - 1)   # 알몸인 경우를 제외하므로 1 뺌
