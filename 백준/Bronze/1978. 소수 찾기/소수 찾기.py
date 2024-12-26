n = int(input())
arr = list(map(int, input().split()))

result = 0
for x in arr:
	for i in range(2, x+1):
		if x % i == 0:
			if x == i:
				result += 1
			break
		
print(result)