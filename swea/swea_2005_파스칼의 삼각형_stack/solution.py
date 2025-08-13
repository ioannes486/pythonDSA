import sys
sys.stdin = open("input.txt", "r")




def solve(N):

    source_stack = []
    target_stack = []

    for i in range(N):
        for j in range(i+1):
            if j==0 or j==i:
                target_stack.append(1)
            else:
                target_stack.append(source_stack.pop() + source_stack[-1])
            print(target_stack)
            source_stack ,target_stack = target_stack, source_stack

T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    # 출력
    print(f"#{test_case}")
    solve(N)