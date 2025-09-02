import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def solve(decimal_number):

    result = ""

    while decimal_number > 0 and len(result) < 13:
        if 2 * decimal_number - 1 > 0:
            result += "1"
            decimal_number = 2 * decimal_number - 1
        elif 2 * decimal_number - 1 < 0:
            result += "0"
            decimal_number = 2 * decimal_number
        else:
            result += "1"
            return result
    return "overflow"


T = int(input())
for test_case in range(1, T + 1):
    decimal_number = float(input())

    # 출력
    print(f"#{test_case} {solve(decimal_number)}")