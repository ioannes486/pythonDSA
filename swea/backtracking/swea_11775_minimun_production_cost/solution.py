import sys
sys.stdin = open("input2.txt", "r")

"""TODO:
- 상수

- 변수
    N : 공장과 제품의 종류
- 조건(제약사항)
    
- 구하는 값
    전체 제품의 최소 생산비용 계산하기
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


path = []
def perm(factory_idx, cursum):

    global result

    if cursum >= result:
        return

    if factory_idx == N:
        result = min(cursum, result)
        return

    for product_idx in range(0, N):


        if used[product_idx]:
            continue

        used[product_idx] = True
        perm(factory_idx + 1, cursum + factories[product_idx][factory_idx])
        used[product_idx] = False




T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    result = 99 * N
    perm(0, 0)

    # 출력
    print(f"#{test_case} {result}")