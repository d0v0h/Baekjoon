import sys
input = sys.stdin.readline

def round_up(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

t = int(input())

cut_line = round_up(t * 0.15)

result = []
for _ in range(t):
    num = int(input())
    result.append(num)

result.sort()
result = result[cut_line:t-cut_line]
if t == 0:
    print(0)
else:
    print(round_up(sum(result)/len(result)))