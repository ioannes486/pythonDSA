import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    리스트 안의 수는 백만 이하임
- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def is_condition_satisfied(target):


    l = 0
    r = N - 1

    state = None
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == target:
            return True

        elif A[mid] > target:  # 타겟이 작으면 왼쪽 서치
            if state == 1:
                return False
            state = 1
            r = mid - 1

        elif A[mid] < target:  # 타겟이 크면 오른쪽 서치\
            if state == 2:
                return False
            state = 2
            l = mid + 1

    return False


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int,input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    result = 0
    for item in B:
        if is_condition_satisfied(item):
            result += 1

    # 출력
    print(f"#{test_case} {result}")