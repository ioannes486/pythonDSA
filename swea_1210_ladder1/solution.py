import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    도착점의 값 : 2
    사다리 : 1
    빈칸 : 0
    사다리 크기 100 바이 100
- 변수
    테스트 케이스
    도착점의 인덱스

- 조건(제약사항)
    사다리 걸리는 사람이 이아스크림 사야함
    김대리가 사다리 그림
    2부터 출발해서 출발점까지 거꾸로 가보자

- 구하는 값

- 아이디어
    간격 두개가 붙어있는 일은 없을 듯

사다리의 크기는 모지?
"""
class Directions:
    LEFT = "left"
    RIGHT = "right"
    VERTICAL = "vertical"

def decide_direction(i_idx, j_idx, direction, is_vertical):
    condition_vertical = arr[i_idx - 1][j_idx] == 1

    # j_idx가 양 극단에 있을 경우와 그렇지 않을 경우 탐색 분기하기
    if j_idx == 0:  # 사다리 왼쪽 끝이면 왼쪽 조건은 무조건 0
        condition_left = 0
        condition_right = arr[i_idx][j_idx + 1] == 1

    elif j_idx ==99: # 사다리 오른쪽 끝이면 오른쪽 조건은 무조건 0
        condition_right = 0
        condition_left = arr[i_idx][j_idx - 1] == 1
    else:
        condition_left = arr[i_idx][j_idx - 1] == 1
        condition_right = arr[i_idx][j_idx + 1] == 1

    #    1
    #  1 1 0 이 모양일 경우
    if condition_left and condition_vertical:
        if is_vertical:
            direction = Directions.LEFT
            is_vertical = False
        else:
            direction = Directions.VERTICAL
            is_vertical = True

    #   1
    # 0 1 1 이 모양일 경우
    elif condition_right and condition_vertical:
        if is_vertical:
            direction = Directions.RIGHT
            is_vertical = False
        else:
            direction = Directions.VERTICAL
            is_vertical = True


    return direction, is_vertical

def solve(arr, x_idx):

    # 방향 초기화
    direction = Directions.VERTICAL
    is_vertical = True

    # 현재 위치 초기화
    i_idx = 99
    j_idx = x_idx

    # while문에 대해 방향 결정한 다음 나아가기
    while i_idx > 0:
        direction, is_vertical = decide_direction(i_idx, j_idx, direction, is_vertical)
        if direction == Directions.LEFT:
            j_idx -= 1
        elif direction == Directions.RIGHT:
            j_idx += 1
        elif direction == Directions.VERTICAL:
            i_idx -= 1
    return j_idx

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    # 입력
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점의 인덱스 초기화
    x_idx = 0

    # 도착점의 인덱스 구하기
    for i in range(100):
        if arr[99][i] == 2:
            x_idx = i
            break

    # 출력
    print(f"#{N} {solve(arr, x_idx)}")

