import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N: 직원의 수, 해야 할 일의 수 1이상 16이하
- 조건(제약사항)

- 구하는 값
    주어진 일이 모두 성공할 확률의 최댓값 -> 모든 확률을 곱했을 때의 최댓값
    퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력한다.
    하나씩 배분함으로 동시에 여려 직원이 하나의 일을 맡거나 그 반대의 수는 존재하지 않는다.
- 아이디어
"""


# def recur(factory_idx, cost_sum):
#     global result
#
#     if cost_sum >= result:
#         return
#
#     if factory_idx == N:
#         result = min(cost_sum, result)
#         return
#
#
#     for cost_idx in range(N):
#         recur(factory_idx + 1, cost_sum + factories[cost_idx][factory_idx])


def recur(j, curmul):

    global result

    if j == N:
        result = max(result, curmul)
        return

    if result >= curmul:
        return

    for i in range(N):

        if used[i]:
            continue

        used[i] = True
        recur(j + 1, curmul * arr[i][j] / 100)
        used[i] = False







T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    used = [False] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_per = 0
    result = -1
    recur(0, 1)
    # 출력
    print(f"#{test_case}{result*100: .6f}")