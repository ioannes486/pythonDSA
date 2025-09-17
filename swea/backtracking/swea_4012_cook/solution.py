import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    등산로는 가장 높은 봉우리에서 시작해야 한다
    높은 지형에서 낮은 지형으로 연결되어야 한다.
    높이가 같은 곳 또는 낮은 지형이나 대각선 방향의 연결은 불가능하다
    등산로를 만들기 위해 딱 한곳을 정해서 최대 k깊이 만큼 지형을 깎는 공사를 할 수 있다.
    
- 구하는 값

- 아이디어
"""

def synerge(li):
    length = len(li)

    A = 0
    B = 0
    for i in range(N):
        for j in range(N):
            if i in path and j in path:
                A += arr[i][j]
                continue
            if j not in path and i not in path:
                B += arr[i][j]
                continue

    result = abs(A-B)
    return result


def recur(start, r):
    global result
    if r == 0:
        result = min(synerge(path), result)
        # print(path)
        return

    for i in range(start, N):
        path.append(i)
        recur(i + 1, r - 1)
        path.pop()


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    path = []
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 99999999999999999999999999999999
    recur(0, N // 2)
    # 출력
    print(f"#{test_case} {result}")
