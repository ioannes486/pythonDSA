import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
. 스택에서 숫자를 꺼내 출력한다
256자 이내의 연산코드
- 변수

- 조건(제약사항)
    연산자와 피연산자는 여백으로 구분
- 구하는 값
    코드의 연산결과
- 아이디어
"""

def solve(operators):
    stack = [0]* 256
    top = -1
    for operator in operators:
        if operator not in '+-*/.':
            top += 1
            stack[top] = operator

        else:
            if operator == '.':
                if top > 0:
                    return "error"
                else:
                    return stack[top]
            if top >= 1:
                # 두 피연산자의 pop연산
                right_operand = int(stack[top])
                top -= 1
                left_operand = int(stack[top])

                # 계산하기
                if operator == '+':
                    stack[top] = left_operand + right_operand
                elif operator == '-':
                    stack[top] = left_operand - right_operand
                elif operator == '*':
                    stack[top] = left_operand * right_operand
                elif operator == '/':
                    stack[top] = left_operand // right_operand
            else:
                return "error"

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    operators = list(input().split())
    # 출력
    print(f"#{test_case} {solve(operators)}")