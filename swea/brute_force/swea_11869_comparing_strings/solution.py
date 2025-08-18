import sys
sys.stdin = open("input.txt")

def solve(str1, str2):
    N = len(str1)
    M = len(str2)

    for i in range(M-N+1):
        idx = i
        while idx < i+N and str1[idx-i] == str2[idx]:
            idx += 1

        if idx == i+N:
            return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    str1 = input()
    str2 = input()
    # 출력
    print(f"#{test_case} {solve(str1, str2)}")