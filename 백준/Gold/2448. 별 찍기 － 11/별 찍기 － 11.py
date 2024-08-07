n = int(input())

def sol(N):
    if N == 3:
        star = ['  *  ', ' * * ', '*****']
        return star
    
    # step 0: 이전 N에 대한 삼각형을 호출한다. (재귀)
    prev = sol(N // 2)
    result = []
    # step 1: N에 대해 공백을 맞춰준다
    for star in prev:
        result.append(' ' * (N // 2) + star + ' ' * (N // 2))
    
    # step 2: 남은 삼각형을 채워준다.
    for star in prev:
        result.append(star + ' ' + star)
    
    # N에 대한 결과를 return
    return result

for star in sol(n):
    print(*star, sep='')