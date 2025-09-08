import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 선의 개수
- 조건(제약사항)
    끝접이 같은 경우는 없으나 교차하는 경우는 있다
    -> 교차하는 경우 시작 점을 뺀게 양수고 도착점을 뺀게 음수인 경우
    또는 반대의 경우
- 구하는 값
    교차점의 개수 출력하기
- 아이디어
"""

def recur(price, number_of_coins):
    global result
    if price > amount:
        return

    if price == amount:
        result = min(result, number_of_coins)
        return

    if number_of_coins >= result:
        return

    for coin in coins:
        recur(price + coin, number_of_coins + 1)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    amount = int(input())

    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)

    max_coin = coins[0] // coins[-1]

    result = float('inf')
    recur(0,0)
    # 출력
    print(f"#{test_case} {result}")