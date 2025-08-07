import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수 
chill할 영역의 개수 N : 2이상 30 이하

모서리 인덱스와 색상 정보
- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어

좌표와 색깔을 각각 다로 받음, 팔레트를 만들어서 색깔에 해당하는 영역을 더한 후 숫자가 3인 영역의 개수 세기
1이면 red
"""

def paint(palette, dowhajee):  # void
    strt_i, strt_j, due_i, due_j, color = palette

    # 순회돌면서 도화지에 칠하기
    for i in range(strt_i, due_i+1):
        for j in range(strt_j, due_j+1):
            if dowhajee[i][j] == 0:
                dowhajee[i][j] += color

            elif dowhajee[i][j] == 1:  # 빨강으로 칠해져 있는 경우 파란색만 chill할 수 있음
                if color == 2:
                    dowhajee[i][j] += color

            elif dowhajee[i][j] == 2:  # 파랑으로 칠해져 있는 경우 빨간 색만 chill할 수 있음
                if color == 1:
                    dowhajee[i][j] += color



def solve(N, arr):
    cnt = 0
    dowhajee = [[0 for _ in range(10)] for _ in range(10)]

    # 도화지 순회 돌면서 색칠하기
    for palette in arr:
        paint(palette, dowhajee)

    # 순회 돌면서 3값 세기
    for line in dowhajee:
        for dot in line:
            if dot == 3:
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 출력
    print(f"#{test_case} {solve(N, arr)}")