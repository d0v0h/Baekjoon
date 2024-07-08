import sys
input = sys.stdin.readline

n = int(input())

arr = []
count = {}
for _ in range(n):
    num = int(input())
    arr.append(num)
    
    if num not in count.keys():
        count[num] = 1
    else:
        count[num] += 1

arr.sort()
count = sorted(count.items())

print(round(sum(arr) / len(arr)))   # 평균 출력
print(arr[n//2])                    # 중간값 출력

max_count = 0
min_value = 4001

for c in count:
    if c[1] > max_count:
        max_count = c[1]
        result = []
        result.append(c[0])
    elif c[1] == max_count:
        result.append(c[0])

try:
    print(result[1])
except:
    print(result[0])
print(arr[-1] - arr[0])