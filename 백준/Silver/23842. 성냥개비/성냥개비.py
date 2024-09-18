import sys; sys.setrecursionlimit(10**9)

N = int(input())
n = (N-4)
arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if n == arr[a] + arr[b] + arr[c] + arr[d] + arr[e] + arr[f]:
                            if (a * 10 + b) + (c * 10 + d) == (e * 10 + f):
                                print(f'{a}{b}+{c}{d}={e}{f}')
                                exit()
print('impossible')