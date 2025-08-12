import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수
    N = 글자판의 크기
    M = 회문의 크기
- 변수
    글자 배열
- 조건(제약사항)
    회문은 1개가 존재함
    가로뿐만아니라 세로로 찾아질 수도
    
- 구하는 값
    길이가 Md인 회문 찾아 출력하기
- 아이디어
    일단 배열에 넣기
    is_palindrome함수 사용하기
"""
def is_palindrome(M, char_list):
    for i in range(M//2):
        if char_list[i] != char_list[M-i-1]:
            return False
    return True


def solve(N, M, arr):

    for i in range(N):
        for j in range(N-M+1):
            char_list1 = [0] * M
            char_list2 = [0] * M
            for k in range(M):
                char_list1[k] = arr[i][j+k]
                char_list2[k] = arr[j+k][i]
                if is_palindrome(M, char_list1):
                    return "".join(char_list1)
                elif is_palindrome(M, char_list2):
                    return "".join(char_list2)


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 출력
    print(f"#{test_case} {solve(N, M,arr)}")