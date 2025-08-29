import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    거울은 2가지 방향만을 가진다
    맨 처음 출발은 0,0에서 오른쪽이다
    0 : 아무것도 없는 공간
    1 : / 거울
    2 : \ 거울
- 변수
    N : 배열의 크기
- 조건(제약사항)
    N은5 이상 100이하
    0,0에는 거울이 없다
- 구하는 값
    격자판 밖으로 나갈 때까지 몇개의 거울에 레이저가 반사되는디
- 아이디어
    거북이 문제랑 똑같은 듯?
    종료조건이 필요할 듯 하다. 재귀함수는 필요 없고 while로 i_idx와 j_idx가 범위 밖을 나가면 종료할듯
    반사라는 것에 대한 정의가 필요함 -> dj, di의 인덱스가 바뀐다.
    1번 거울: 수평방향에서 오면 좌회전 idx -1, 수직방향에서 오면 우회전 idx +1
    2번 거울 : 수평방향에서 오번 우회전 idx +1, 수직방향에서 도면 좌회전 idx-1
    수평방향에서 온다. -> 지금 방향의 idx가 0이거나 짝수다
    수직 방향에서 온다 -> 지금 방향의 idx가 홀수다
    
"""
#    >  아  < ^
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def solve(N, arr):

    reflection_count = 0
    # 현재 위치의 i,j좌표 초기화
    i_idx = 0
    j_idx = 0

    direction_idx = 0  # 처음엔 우측방향

    # 레이저가 배열 안에 있을 때
    while 0 <= i_idx < N and 0 <= j_idx < N:

        # 전진
        if arr[i_idx][j_idx] == 0:
            i_idx += di[direction_idx]
            j_idx += dj[direction_idx]

        # 거울 1을 만날 경우
        elif arr[i_idx][j_idx] == 1:
            reflection_count += 1
            # 수평 방향일 경우
            if direction_idx % 2 == 0:
                # 좌회전 하기
                direction_idx = (direction_idx + 3) % 4
            # 수직 방향일 경우
            else:
                # 우회전 하기
                direction_idx = (direction_idx + 1) % 4
            i_idx += di[direction_idx]
            j_idx += dj[direction_idx]

        # 거울 2를 만날 경우
        elif arr[i_idx][j_idx] == 2:
            reflection_count += 1

            # 수평 방향일 경우
            if direction_idx % 2 == 0:
                # 우회전 하기
                direction_idx = (direction_idx + 1) % 4

            # 수직 방향일 경우
            else:
                # 좌회전 하기
                direction_idx = (direction_idx + 3) % 4
            i_idx += di[direction_idx]
            j_idx += dj[direction_idx]

    return reflection_count


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 출력
    print(f"#{test_case} {solve(N, arr)}")
