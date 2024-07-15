import sys
input = sys.stdin.readline

t = int(input())
schedule = list(map(int, input().split()))

schedule.sort()
result = 0
for i in range(1, len(schedule)+1):
    result += sum(schedule[0:i])

print(result)