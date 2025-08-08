import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    각 단어의 길이는 3이상 10 이하이다
- 구하는 값

- 아이디어
"""

def solve(text):
    text_length = len(text)
    for i in range(text_length-1):
        if text[i] != text[text_length-i-1]:
            return 0
    return 1


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    text = input()
    # 출력
    print(f"#{test_case} {solve(text)}")