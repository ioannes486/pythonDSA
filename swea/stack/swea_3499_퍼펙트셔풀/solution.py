import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수
    N : 카드의 수
- 조건(제약사항)
    N이 홀수이면 교대로 놓을 때 먼저 놓는 쪽에 한장이 더 들어가게 하면 된다.
    -> 짝수일 경우에도 마찬가지
    카드는 공백으로 구분되어 출력됨
    카드의 이름은 알파벳 대문자와 -만으로 이루어져 있음 길이는 80이하
- 구하는 값
    퍼펙트 셔풀하면 어떤 순서가 되는지 
- 아이디어
   i의 나머지가 0이면 선행 스택에
    i의 나머지가 1이면 후행스택에 쌀기
"""

def solve(N, deck):
    first_stack = []
    second_stack = []
    shuffled_stack = []

    for i in range(N):
        if i < N/2:
            first_stack.append(deck[i])

        else:
            second_stack.append(deck[i])

    if len(first_stack) > len(second_stack):
        for i in range(N//2):
            shuffled_stack.append(first_stack.pop())
            shuffled_stack.append(second_stack.pop())
    else:
        for i in range(N//2):
            shuffled_stack.append(second_stack.pop())
            shuffled_stack.append(first_stack.pop())

    if first_stack:
        shuffled_stack.append(first_stack.pop())

    return " ".join(reversed(shuffled_stack))

8
T = int(input())
for test_case in range(1, T + 1):
    # 입력
    N = int(input())
    deck = input().split()

    # 출력
    print(f"#{test_case} {solve(N, deck)}")