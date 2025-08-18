import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    문자 배열의 크기 100
    회문의 가능한 최대 길이 100
    
- 변수
    회문의 길이
- 조건(제약사항)
    각 칸의 들어가는 글자는ABC중에 하나
    글자 판은 무조건 정사각형
    A도 길이 1짜리 회문임
    
- 구하는 값
    가장 긴 회문의 `길이` => 길이만 구하면 됨
    
- 아이디어

    for 문을 100부터 0까지 차례로 돌면서 가장 긴 길이를 구하기
"""

def solve(arr):

    for N in range(100, 0, -1):
        for i in range(101-N):
            for j in range(101-N):

                idx = 0
                while idx < (N//2) and arr[i][j+idx] == arr[i][j+N-1-idx]:
                    idx += 1

                if idx == (N//2):
                    return N

                idx = 0
                while idx < (N // 2) and arr[j + idx][i] == arr[j+N-1-idx][i]:
                    idx += 1

                if idx == (N // 2):
                    return N

T = 10
for test_case in range(1, T + 1):
    # 입력
    tc = int(input())
    arr = [list(input()) for _ in range(100)]


    # 출력
    print(f"#{test_case} {solve(arr)}")
