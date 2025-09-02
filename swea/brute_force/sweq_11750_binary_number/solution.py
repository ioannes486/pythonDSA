import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""


hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def solve():
    result = ""
    for char in text_arr:
        result += hex_to_bin[char]
    return result


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, text = input().split()

    text_arr = list(text)

    # 출력
    print(f"#{test_case} {solve()}")


