import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    A, B
- 조건(제약사항)
    A의 길이는 1이상 10000이하
    B의 길이는 1이상 100이하
    
- 구하는 값
    키를 눌러야 하는 횟수의 최솟값
- 아이디어
    여러군데에 적용을 할 수 있는 경우
"""

def count_length(txt):
    length = 0
    for _ in txt:
        length+=1
    return length

def solve(A, B):

    A_length = count_length(A)
    B_length = count_length(B)

    B_count = 0

    A_idx = 0
    while A_idx < A_length-B_length+1:
        B_idx = 0
        while B_idx < B_length and A[A_idx+B_idx] == B[B_idx]:
            B_idx += 1
        if B_idx == B_length:
            B_count += 1
            A_idx += B_length
        else:
            A_idx += 1
    result = A_length - (B_length-1) * B_count
    return result

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    A, B = input().split()
    # 출력
    print(f"#{test_case} {solve(A, B)}")