import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    8 개의 숫자로 이루어져 있는 암호
    암호코드는 7개의 비트로 암호화된
- 변수

- 조건(제약사항)

- 구하는 값
    암호코드에 포함된 숫자의 값
- 아이디어
    세가지 구현
    1. 입출력 받아서 암호 부분만 도려내기
    2. 암호화의 진법변환을 적용하여 암호를 올바른 10진수로 바꾸기
    3. 각 자리수를 더해서 홀수자리번째 * 3 더하기 짝수 자리번째가 10의 배수인지 확인하기
    4 숫자의 합 구하기
"""

encryption_map = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}


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

# 1. 56자리 암호를 파싱해보자
def convert_hex_line_to_binary(line):
    binary_line = ""

    for char in line:
        unit = hex_to_bin[char]
        binary_line += unit

    return binary_line


def parse_code(arr):
    # 1. 16진수를 2진수로 변환하기
    codes = []

    for i in range(N):
        line = arr[i]
        if "1" in line:

            # 제일 첫번째 1의 좌표 구하기
            idx = M*4-1
            while line[idx] == "0":
                idx -= 1

            if arr[i-1][idx] == "0":



                # 암호한개찾기
                for _ in range(8):
                    # 첫번째 숫자 구하기
                    target_num = "1"
                    change_cnt = 0
                    ratio = [0, 0, 0, 0]
                    while change_cnt < 4:
                        if line[idx] == target_num:
                            ratio[change_cnt] += 1
                            idx -= 1
                            continue

                        if line[idx] != target_num:
                            change_cnt += 1
                            target_num = str(abs(int(target_num) - 1))
                            continue

                    min_ratio = min(ratio)
                    for i in range(4):
                        ratio[i] //= min_ratio
                    codes.append(ratio)
    return codes





def decrypt_code(code):
    result = ""
    for i in range(0, 56, 7):
        unit_code = code[i:i + 7]
        result += encryption_map[unit_code]

    return result


def validate_code(decrypted_code):
    validation_number1 = 0
    validation_number2 = 0
    for i in range(8):
        if i % 2 == 0:
            validation_number1 += int(decrypted_code[i])
            continue
        if i % 2 == 1:
            validation_number2 += int(decrypted_code[i])
            continue
    if (validation_number1 * 3 + validation_number2) % 10 == 0:
        return validation_number1 + validation_number2
    return 0

def solve(arr):
    codes = parse_code(arr)

    return codes


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    arr = ["" for _ in range(N)]

    for i in range(N):
        line = input()
        arr[i] = convert_hex_line_to_binary(line)




    print(f"#{test_case} {solve(arr)}")

