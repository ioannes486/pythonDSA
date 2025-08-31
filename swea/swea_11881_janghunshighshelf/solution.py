import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)
    사다리게임이 지겹다
    이게 대체 무신 말이지...
- 구하는 값

- 아이디어
    부분집합의 합으로 푸는 문제임
"""


def process_solution(bit, arr):
    subset = [arr[i] for i in range(N) if bit[i] == 1]
    return sum(subset)

def solve():

    bit = [0] * N

    def recur(idx):
        global answer

        if idx == N:
            subset_sum = process_solution(bit, arr)
            if subset_sum >= B:
                answer = min(answer, subset_sum)

        else:
            for c in (0,1):
                bit[idx] = c
                if recur(idx + 1) == B:
                    return B

    recur(0)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N,B = map(int, input().split())

    arr = list(map(int, input().split()))
    answer = 9999999999

    solve()
    answer = answer - B
    # 출력
    print(f"#{test_case} {answer}")