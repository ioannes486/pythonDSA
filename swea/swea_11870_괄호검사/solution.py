import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    문자열
- 조건(제약사항)
    온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어짐
- 구하는 값
    주어진 입력에서 괄호가 제대로 짝을 이뤘으면 1 이루지 않았으면 0
- 아이디어
    이건 지원이가 알려준 방법이 맞는 듯?
"""

def solve(text):

    size = len(text)
    stack = [0]*size
    top = -1
    flag1 = False
    flag2 = False
    for char in text:
        flag1 = True
        if char in ['(','{']:
            flag2 = True
            top += 1
            stack[top] = char

        elif char == '}':
            if top == -1:
                return 0

            if stack[top] == '(':
                return 0

            if stack[top] == '{':
                top -= 1

        elif char == ')':
            if top == -1:
                return 0

            if stack[top] == '{':
                return 0

            if stack[top] == '(':
                top -= 1

    if top == -1 and flag2 and flag1:
        return 1

    return 0



T = int(input())
for test_case in range(1, T + 1):
    # 입력
    text = input()
    # 출력
    print(f"#{test_case} {solve(text)}")