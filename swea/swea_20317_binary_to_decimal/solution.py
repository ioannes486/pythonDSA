import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""


def binary_to_decimal(binary_number):
    result = 0

    for i in range(7):
        if binary_number[i] == '1':
            result += 2**(6-i)
    return result

def solve(binary_numbers):
    result = ""
    for idx in range(0, len(binary_numbers), 7):
        binary_number = ""
        for j in range(idx, idx+7):
            binary_number += binary_numbers[j]

        result += str(binary_to_decimal(binary_number))
        result += " "

    return result.rstrip()


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    binary_numbers = input()

    # 출력
    print(f"#{test_case} {solve(binary_numbers)}")