import sys; input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []        # N-S
    dp_rev = []    # S-N

    # 이웃 자석 값 초기화
    for i in range(n-1):
        dp.append(arr[i] - arr[i+1] - k)
    
    for i in range(n-1, 0, -1):
        dp_rev.append(arr[i] - arr[i-1] - k)
    result, result_rev = [0] * (n-1), [0] * (n-1)
    result[0], result_rev[0] = dp[0], dp_rev[0]
    for i in range(n-2):
        # max(0, result[i])는 에너지 충전량이 음수인 경우 다음 순번을 고려하는 코드
        result[i+1] = ((max(0, result[i])) + dp[i+1])
        result_rev[i+1] = ((max(0, result_rev[i])) + dp_rev[i+1])
    print(max(max(result), max(result_rev)))