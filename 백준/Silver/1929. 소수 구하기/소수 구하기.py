m, n = map(int, input().split())

# 학교 알고리즘 수업 시간에 배운 코드 응용
def eratos(arr):
    arr[0] = arr[1] = 0
    i = 2
    # 2와 3은 소수이므로 계산에서 제외
    while i * i <= n:
        j = 2
        # j를 1씩 증가시키며 소수가 아닌 수를 0으로 초기화
        while i * j <= n:
            arr[i*j] = 0
            j += 1
        i += 1 
    return arr

num = list(range(n+1))
result = eratos(num)[m:]

for r in result:
    if r != 0:
        print(r)