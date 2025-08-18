import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    각 괄호의 종류
- 변수
    각 문자열의 길이
    문자열
- 조건(제약사항)
    10개의 테스트케이스
- 구하는 값
    유효성 여부를 1또는 0으로 표시
- 아이디어
    어떤 값이 남아있든 간에 조건을 만족시키지 않으면
        1. 닫는 괄호가 먼저 나오는 경우
        2. 연산이 끝나고도 하는  스택에 자료가 계속 남아있는 경우
        
    0을 반환해야함, 이때 스택의 길이를 충분히 길게 해주어서 스택오버플로우는 안됨
"""

def solve(N,text):
    p_top = -1
    s_top = -1
    c_top = -1
    b_top = -1

    p_stack = [0] * N
    s_stack = [0] * N
    c_stack = [0] * N
    b_stack = [0] * N

    for char in text:
        if char == '(':
            p_top += 1
            p_stack[p_top] = '('
        elif char == ')':
            if p_top == -1:
                return 0
            else:
                p_top -= 1

        elif char == '[':
            s_top += 1
            s_stack[s_top] = '['
        elif char == ']':
            if s_top == -1:
                return 0
            else:
                s_top -= 1

        elif char == '{':
            c_top += 1
            c_stack[c_top] = '{'
        elif char == '}':
            if c_top == -1:
                return 0
            else:
                c_top -= 1

        elif char == '<':
            b_top += 1
            b_stack[b_top] = '<'
        elif char == '>':
            if b_top == -1:
                return 0
            else:
                b_top -= 1

    if p_top != -1:
        return 0
    if s_top != -1:
        return 0
    if c_top != -1:
        return 0
    if b_top != -1:
        return 0

    return 1

T = 1
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    text = input()
    # 출력
    print(f"#{test_case} {solve(N,['(','(','(','{',')','}',')',')'])}")