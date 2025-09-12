import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    모든 종류의 이용권 요금은 10 이상 3000이하의ㅣ 정수
    각 달의 이용계획은 각 달의 마지막 일자보다 크지 않다. 전부 31이하이다.
- 구하는 값

- 아이디어
"""

def recur(idx, curcost):
    global result

    if idx > 12:
        return

    if idx == 12:
        result = min(curcost, result)
        return

    if curcost >= result:
        return


    # 해당 월에 하루 요금만 내는 경우
    recur(idx + 1, curcost + cost_1day * plan[idx])

    # 해당 월에 한달 요금을 내는 경우
    recur(idx + 1, curcost + cost_1month)

    # 해당 월에 3달 요금을 내는 경우
    recur(idx + 3, curcost + cost_3month)

    # 해당 월에 1년 요금을 내는 경우
    recur(idx + 12, curcost + cost_1year)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    cost_1day, cost_1month, cost_3month, cost_1year = map(int, input().split())

    plan = list(map(int, input().split()))
    result = float('inf')

    recur(0, 0)

    # 출력
    print(f"#{test_case} {result}")