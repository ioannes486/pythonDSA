import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    
- 변수

- 조건(제약사항)
    왼쪽 괄호의 개수와 오른쪽괄호의 개수가 같아야 한다
    같은 괄호에서 왼쪽괄호는 오른쪽 괄호보다 먼저 나와야 한다
    괄호 사이에는 포함관계만 존재한다.
- 구하는 값
    주어진 괄호에 대해 짝이 맞으면 1, 안맞으면 0
- 아이디어
"""
LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"


def solve(parentheses):
    top = -1
    stack = [0] * (len(parentheses) + 1)

    for parenthesis in parentheses:
        if parenthesis == LEFT_PARENTHESIS:
            top += 1
            stack[top] = parenthesis
        elif parenthesis == RIGHT_PARENTHESIS:
            if top == -1:
                return 0
            else:
                top -= 1

    if top == -1:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    parentheses = input()

    # 출력
    print(f"#{test_case} {solve(parentheses)}")
