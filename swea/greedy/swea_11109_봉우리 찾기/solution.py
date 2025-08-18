import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 지형의 높이 의 수
    지형의 높이 : 0보다 크고 10보다 작음
- 조건(제약사항)
    높아지다가 낮아지는 지형을 봉우리로 간주한다
    맨 앞쪽 지형은 다음 지형보다 높으면 봉우리임 -> 오타 난듯
    맨 뒤쪽 지형은 이전지형보다 높으면 봉우리고 간주
    지형이 1개여도 1개의 봉우리임
- 구하는 값
    봉우리의 수
- 아이디어
    그리디 문제인듯
    봉우리의 크기가 커
"""

def solve(N, arr):
    if N == 1:
        return 1

    bongwoori_state = -1
    bongwoori_count = 0
    for i in range(N-1):
        if bongwoori_state == 0:
            bongwoori_count += 1

        if arr[i] <= arr[i+1]:
            bongwoori_state = -1

        elif arr[i] > arr[i+1]:
            bongwoori_state += 1


    if bongwoori_state == 0:
        bongwoori_count += 1

    if arr[N-1] > arr[N-2]:
        bongwoori_count += 1
    return bongwoori_count


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = list(map(int, input().split()))
    # 출력
    print(f"#{test_case} {solve(N, arr)}")