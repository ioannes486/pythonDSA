# import sys
# sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 배열의 크기
- 조건(제약사항)
    가로로 한번, 세로로 한번 잘라서 딸기의 개수를 정확하게 사등분 하고자 한다
    N은 5이상 100이하이다
    딸기의 개수는 1이상 100,000이하이다
- 구하는 값
    사등분이 가능할 경우 1, 불가능할 경우 0을 출력
- 아이디어
"""


def solve(N, strawberries):
    # 구분선이 각각 1, 1에있을 때 딸기 나누기

    for line_i in range(1, N):
        for line_j in range(1, N):
            num_of_strawberries_in_1 = 0
            num_of_strawberries_in_2 = 0
            num_of_strawberries_in_3 = 0
            num_of_strawberries_in_4 = 0

            # 1. 왼쪽 위 영역의 딸기 더하기
            for i in range(line_i):
                for j in range(line_j):
                    num_of_strawberries_in_1 += strawberries[i][j]

            # 2. 오른쪽 위 영역의 딸기 더하기
            for i in range(line_i):
                for j in range(line_j, N):
                    num_of_strawberries_in_2 += strawberries[i][j]

            # 3. 왼쪽 아래
            for i in range(line_i, N):
                for j in range(line_j):
                    num_of_strawberries_in_3 += strawberries[i][j]

            # 4. 오른쪽 아리
            for i in range(line_i, N):
                for j in range(line_j, N):
                    num_of_strawberries_in_4 += strawberries[i][j]

            if (
                num_of_strawberries_in_1
                == num_of_strawberries_in_2
                == num_of_strawberries_in_3
                == num_of_strawberries_in_4
            ):
                return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    strawberries = [list(map(int, input().split())) for _ in range(N)]
    # 출력
    print(f"#{test_case} {solve(N, strawberries)}")
