import sys
from collections import deque
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    주어지는 문자열
- 조건(제약사항)
    연결에 의해 또 반복문자가 생기면 이 부분을 다시 지운다
    문자열 길이는 1000이내
- 구하는 값
    문자열 제거 후 남은 문자열의 길이
- 아이디어
    스택연산 후 최후의 top을 추출한다
    근데 홀수 문자열은 어떻게 하지?
    남은 문자열의 최솟값도 있지 않나?
    그러면 상관없을 가능성?
    
    홀수개가 연달아 있으면 지운다
    맨 마지막 문자가 어떤 문자인지 담은 변수 하나 만들기
    
    하나가 동떨어져 있으면 그 하나는 남을 수도 있고
"""

def solve(text):
    stack = deque()
    for char in text:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    return len(stack)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    text = input()
    # 출력
    print(f"#{test_case} {solve(text)}")