from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

max = 0
queue = deque()
result = ''
for _ in range(n):
    num = int(input())

    try:
        if num > queue[-1]:
            for i in range(max+1, num+1):
                queue.append(i)
                result += '+'
            output = queue.pop()
            if output > max:
                max = output
            result += '-'
        elif num == queue[-1]:
            queue.pop()
            result += '-'
        else:
            print('NO')
            break
    except:
        for i in range(max+1, num+1):
            queue.append(i)
            result += '+'
        output = queue.pop()

        if output > max:
            max = output
        result += '-'
    
else:
    print(*result, sep='\n')
    