import sys
input = sys.stdin.readline

n = int(input())

slot_machine = []
for i in range(3):
    wheel = list(map(int, input().split()))
    if 7 in wheel:
        slot_machine.append(wheel)
    else:
        break

if len(slot_machine) == 3:
    print(777)
else:
    print(0)
