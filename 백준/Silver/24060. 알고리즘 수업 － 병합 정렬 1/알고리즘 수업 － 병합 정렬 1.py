def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    global cnt
    i, j, k = left, mid + 1, left

    # 두 개의 리스트 비교 후 정렬
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    # 왼쪽 배열에 남은 값
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    # 오른쪽 배열에 남은 값
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]
        cnt += 1
        
        if cnt == K:
            print(arr[i])
            exit(0)


cnt = 0
n, K = map(int, input().split())
a = list(map(int, input().split()))

temp = [0] * n

merge_sort(a, 0, n-1)

print(-1)