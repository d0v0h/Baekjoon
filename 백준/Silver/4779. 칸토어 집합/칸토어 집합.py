def sol(n):
    if n == 1:
        return '-'
    left = sol(n // 3)
    cent = ' ' * (n // 3)
    return left + cent + left

while True:
    try:
        n = int(input())
        print(sol(3 ** n))
    except:
        break