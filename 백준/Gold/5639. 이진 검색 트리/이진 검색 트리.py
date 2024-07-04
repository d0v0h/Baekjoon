import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    # mid: start기준 오른쪽 노드가 발생하는 지점
    # 초기에는 없다고 가정
    mid = end + 1

    for i in range(start+1, end+1):
        # start노드보다 큰 값이 발생하면 해당 노드 인덱스는 오른쪽 노드이므로 mid 갱신
        if tree[i] > tree[start]:
            mid = i
            break
    postorder(start+1, mid-1)   # 왼쪽 확인
    postorder(mid, end)         #오른쪽 확인
    print(tree[start])

postorder(0, len(tree)-1)