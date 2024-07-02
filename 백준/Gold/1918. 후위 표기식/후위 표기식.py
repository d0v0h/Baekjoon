postfix = input()
stack = []
result = ''

for char in postfix:
    # 연산자가 아니면 result에 피연산자 추가
    if char.isalpha():
        result += char
    else:
        # 우선순위가 가장 높은 여는 괄호를 스택에 push
        if char == '(':
            stack.append(char)
        # *, /는 연산자 우선순위가 괄호 다음으로 높다. +, -를 만나도 *, /가 먼저 pop되야 하므로 아래 조건 작성
        elif char == '*' or char == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(char)
        # +와 -는 여는 괄호를 만나기 전의 연산자를 모두 출력
        elif char == '+' or char == '-':
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.append(char)
        # 닫는 괄호가 나오면 여는 괄호 이전까지의 연산자를 출력
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            # 여는 괄호는 최종 결과에 안나타나므로 pop으로 없앰
            stack.pop()

# 남은 연산자 출력
while stack:
    result += stack.pop()

print(result)