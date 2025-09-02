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
'0001101' : '0',
'0011001' : '1',
'0010011' : '2',
'0111101' : '3',
'0100011' : '4',
'0110001' : '5',
'0101111' : '6',
'0111011' : '7',
'0110111' : '8',
'0001011' : '9',
}


def parse_code():
    for i in range(N):
        line = input()
        if "1" in line:
            idx = 0
            for j in range(M-1, -1, -1):
                if line[j] == "1":
                    idx = j
                    code = line[j-55:j+1]
                    break
    return code


def decrypt_code(code):
    result = ""
    for i in range(0, 56, 7):
        unit_code = code[i:i+7]
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


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    code = parse_code()
    decrypted_code = decrypt_code(code)
    result = validate_code(decrypted_code)

    # 출력
    print(f"#{test_case} {result}")