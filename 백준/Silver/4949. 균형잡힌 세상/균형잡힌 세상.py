from collections import deque


while True:
    string = input()
    if string == '.':
        break

    stack = deque()
    flag = True
    for char in string:
        if char == '(':
            stack.append('(')

        elif char == '[':
            stack.append('[')

        elif char == ')':
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] != '(':
                flag = False
                break
            stack.pop()

        elif char == ']':
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] != '[':
                flag = False
                break
            stack.pop()

    if flag and len(stack) == 0:
        print('yes')
    else:
        print('no')