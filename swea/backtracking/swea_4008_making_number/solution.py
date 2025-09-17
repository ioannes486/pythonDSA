import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def solve(idx, amount_p, amount_m, amount_mul, amount_d, cur_val):

    global min_result
    global max_result
    if idx == N:
        min_result = min(cur_val, min_result)
        max_result = max(cur_val, max_result)
        return

    if amount_p > 0:
        solve(idx + 1, amount_p-1, amount_m, amount_mul, amount_d, cur_val + numbers[idx])
    if amount_m > 0:
        solve(idx + 1, amount_p, amount_m-1, amount_mul, amount_d, cur_val - numbers[idx])
    if amount_mul > 0:
        solve(idx + 1, amount_p, amount_m, amount_mul-1, amount_d, cur_val * numbers[idx])
    if amount_d > 0:
        solve(idx + 1, amount_p, amount_m, amount_mul, amount_d-1, int(cur_val / numbers[idx]))



T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 9999999999999999999999999999999999999999
    max_result = -9999999999999999999999999999999999999999
    solve(1, operators[0], operators[1], operators[2], operators[3], numbers[0])
    result = max_result - min_result

    # 출력
    print(f"#{test_case} {result}")