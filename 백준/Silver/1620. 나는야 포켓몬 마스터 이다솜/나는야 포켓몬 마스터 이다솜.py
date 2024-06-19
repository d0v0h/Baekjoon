import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_book = {}
for i in range(1, N+1):
    pokemon = input().strip()
    pokemon_book[i] = pokemon
    pokemon_book[pokemon] = i

for i in range(M):
    problem = input().strip()
    if problem.isdigit():
        print(pokemon_book[int(problem)])
    else:
        print(pokemon_book[problem])