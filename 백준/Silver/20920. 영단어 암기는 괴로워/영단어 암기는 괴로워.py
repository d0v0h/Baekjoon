import sys; input = sys.stdin.readline

n, m = map(int, input().split())

note = dict()
for _ in range(n):
    word = input().strip()

    if len(word) >= m:
        if word not in note:
            note[word] = 1
        else:
            note[word] += 1

note = sorted(note, key=lambda x: (-note[x], -len(x), x))
print(*note, sep='\n')