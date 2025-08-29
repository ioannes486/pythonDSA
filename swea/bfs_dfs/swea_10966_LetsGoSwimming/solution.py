import sys

sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    물이면  W,
    땅이면 L
- 변수
    N : 영역의 세로 길이
    M : 영역의 가로 길이
    
- 조건(제약사항)
    
- 구하는 값
    땅으로 표현된 모든 칸에 대해서 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수의 합
    
- 아이디어
    i, j의 모든 칸에 대하여 dfs돌리기
    dfs를 만들어서 W이면 리턴
    
    과연 물로 나가기 전까지 거리를 계산하는 방법은?
    윳놀이 방식
    
    
    
    
    
"""


def solve():

    return


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())

    arr = list(input())
    # 출력
    print(f"#{test_case} {solve()}")
