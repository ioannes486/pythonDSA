import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    
- 조건(제약사항)
    연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    하루 최대 1만큼 구입할 수 있다.
    판매는 얼마든지 할 수 있다.
    
- 구하는 값

- 아이디어
"""

def max_idx(arr):
    if arr:
        max_idx = 0
        for i in range(len(arr)):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx

    return N

def solve():

    outcome = 0
    income = 0
    stock = 0
    max_val = max(stock_prices)
    for i in range(N):
        if stock_prices[i] < max_val:
            outcome += stock_prices[i]
            stock += 1
            continue

        if stock_prices[i] == max_val:
            income += max_val * stock
            stock = 0
            arr = stock_prices[i + 1:]
            if arr:
                max_val = max(stock_prices[i+1:])
            continue

    result = income - outcome
    return result



T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    stock_prices = list(map(int, input().split()))

    # 출력
    print(f"#{test_case} {solve()}")