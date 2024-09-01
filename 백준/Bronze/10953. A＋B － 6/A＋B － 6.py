import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().strip()

    print(int(string[0]) + int(string[2]))