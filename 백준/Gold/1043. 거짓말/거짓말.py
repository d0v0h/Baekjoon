import sys
input = sys.stdin.readline

n, m = map(int, input().split())
known_list = set(map(int, input().split()[1:]))

party = []
for _ in range(m):
    party.append(set(map(int, input().split()[1:])))

for _ in range(m):
    for p in party:
        # p와 known_list의 교집합이 있는 경우
        if p & known_list:
            # knwo_list와 p의 합집합을 known_list에 할당
            known_list = known_list | p

count = 0
for p in party:
    # 교집합이 발생하면 거짓말을 못하므로 continue
    if p & known_list:
        continue
    count += 1

print(count)