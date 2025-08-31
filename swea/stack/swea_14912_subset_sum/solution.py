import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    10개의 정수 입력받기
    0
    
- 변수

- 조건(제약사항)

- 구하는 값
    부분집합의 합이 존재하면 1
    그렇지 않으면 0
- 아이디어
"""


def process_solution(bit, idx, arr):
    subset = [arr[i] for i in range(idx) if bit[i] == 1]
    return sum(subset)

def solve():
    bit = [0]* N
    def recur(idx):

        if idx == N:
           subsetsum = process_solution(bit, idx, arr)
           is_subset_empty = True
           for b in bit:
               if b == 1:
                   is_subset_empty = False
                   break

           if subsetsum == 0 and not is_subset_empty:
               return 1
           return 0
        else:
            c = [0, 1]
            for choice in c:
                # 근데 이렇게 하면 매번 bit가 다르지 않나
                # 어차피 순차적으로 실행하는거라 상관이 없나
                bit[idx] = choice
                if recur(idx+1):
                    return 1

            return 0

    return recur(0)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))

    # 출력
    print(f"#{test_case} {solve()}")