import sys
input = sys.stdin.readline

n, m = map(int, input().split())

problem_count = 0
problem_arr = []
for i in range(n):
    problem = int(input().strip())
    problem_count += problem
    problem_arr.append(problem)

pay = m // problem_count
for i in problem_arr:
    print(i * pay)