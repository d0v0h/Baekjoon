import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

pn = 'IO' * n + 'I'
length = len(pn)

i = cnt = ans = 0

while i < m-1:
    if s[i:i+3] == 'IOI':   # i ~ i+2까지 'IOI'이면
        i += 2              # 2칸 건너 뜀
        cnt += 1            # IOI 하나 발생 체크
        if cnt == n:        # IOI 발생과 pn이 일치하면
            ans += 1        # 정답 카운트 1 증가
            cnt -= 1        # 이동한 슬라이딩 윈도우 왼쪽부분 제거
    
    else:
        i += 1              # IOI가 아니면 한칸 미룸
        cnt = 0             # 연속 IOI가 깨졌으므로 0으로 초기화

print(ans)