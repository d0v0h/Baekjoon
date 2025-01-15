import sys; input = sys.stdin.readline

def sol(hist):
    def largest_area(start, end):
        if start == end:
            return hist[start]
        
        mid = (start + end) // 2

        left_largest = largest_area(start, mid)
        right_largest = largest_area(mid + 1, end)

        width = 1
        height = hist[mid]
        mid_largest = height * width
        left, right = mid, mid

        while start < left or right < end:
            if start < left and ((right == end) or hist[left - 1] >= hist[right + 1]):
                left -= 1
                height = min(height, hist[left])
            else:
                right += 1
                height = min(height, hist[right])
            width += 1
            mid_largest = max(mid_largest, height * width)
        
        # mid를 기준으로 왼쪽, mid를 포함한 넓이, 오른쪽 넓이 중 가장 큰 값 return
        return max(left_largest, mid_largest, right_largest) 

    return largest_area(0, len(hist) - 1)

cmd = list(map(int, input().split()))

while cmd[0] != 0:
    result = sol(cmd[1:])
    print(result)

    cmd = list(map(int, input().split()))
