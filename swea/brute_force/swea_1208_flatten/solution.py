import sys

sys.stdin = open("input.txt", "r")


def solve(attempt_remaining, cnt_arr):
    # 높이 차 초기화
    data = 99
    lidx = 1
    ridx = 100
    while attempt_remaining > 0:

        data = ridx - lidx
        if data == 0:
            return 0

        if data > 1:
            if cnt_arr[lidx] == 0:
                lidx += 1
            elif cnt_arr[ridx] == 0:
                ridx -= 1
            else:
                # 기회 줄이기
                attempt_remaining -= 1

                # 가장 높은 곳에서 가장 낮은 곳 중 하나로 옮김
                # 높은 곳에서 상자 빼기
                cnt_arr[ridx] -= 1
                cnt_arr[ridx - 1] += 1

                # 낮은 곳에서 상자 빼기
                cnt_arr[lidx] -= 1
                cnt_arr[lidx + 1] += 1

        elif data == 1:
            if cnt_arr[lidx] < cnt_arr[ridx]:
                attempt_remaining -= 1
                cnt_arr[ridx] -= 1
                cnt_arr[lidx] += 1

    return data


T = 10
for test_case in range(1, T + 1):
    # 입출력 받기
    attempt_remaining = int(input())
    orginal_arr = list(map(int, input().split()))
    cnt_arr = [0] * 101
    for pile in orginal_arr:
        cnt_arr[pile] += 1

    print(f"#{test_case} {solve(attempt_remaining, cnt_arr)}")
