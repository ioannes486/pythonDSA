import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    ㄴㄴ
- 변수
    테스트 게이스의 길이
    수식
- 조건(제약사항)

- 구하는 값
    후위 표기식으로 바꾸어 계산하는 프로그램
    괄효의 유효성 여부는 항상 옳다
    숫자는 0~9사이의 정수만 주어진다.
- 아이디어
"""
isp = {
    "(": 0,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
}

icp = {
    "(": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
}


def convert_string_to_number(target):
    if isinstance(target, str):
        target = int(target)
    return target


def solve(formula):
    stack = []
    postfix = ""
    for token in formula:

        if token not in "(+-*/)":
            postfix += token
        # 닫는 괄호 만나면 여는 괄호까지 가기
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()

        # 토큰값이 연산자이고 닫는괄호가 아닌 경우
        else:
            # 스택이 비어있거나 여는 괄호면 그냥 집어넣음
            if (not stack) or (token == "("):
                stack.append(token)

            # 스택 제일 위의 원소의 우선순위가 토큰의 우선순위보다 낮은 경우 토큰 집어넣기
            elif isp[stack[-1]] < icp[token]:
                stack.append(token)

            # 스택 제일 위의 원소 우선순위가 들어가는 원소의 우선순위보다 큰 경우
            elif isp[stack[-1]] >= icp[token]:
                while isp[stack[-1]] >= icp[token]:
                    postfix += stack.pop()

                stack.append(token)

    for token in postfix:
        if token not in "+-*/":
            stack.append(token)
        else:
            if len(stack) >= 2:
                b = convert_string_to_number(
                    stack.pop()
                )  # 여기서 인트로 바꿔버리는 거였던 거임
                a = convert_string_to_number(stack.pop())
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a / b)
    return stack[0]


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    formula = input()

    if not formula.startswith("("):
        formula = "(" + formula
    if not formula.endswith(")"):
        formula = formula + ")"

    # 출력
    print(f"#{test_case} {solve(formula)}")
