import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def is_run_or_triplet(deck):
    deck.sort()
    deck_length = len(deck)
    # run인지 확인
    deck_set = list(set(deck))
    deck_set_length = len(deck_set)
    if deck_set_length >= 3:
        for i in range(deck_set_length-2):
            if deck_set[i] + 2 == deck_set[i+1] + 1 == deck_set[i+2]:
                return True


    for i in range(deck_length-2):
        if deck[i] == deck[i+1] == deck[i+2]:
            return True

    return False

def solve():

    idx = 3
    while idx <= 6:
        if is_run_or_triplet(deck1[:idx]):
            return 1

        if is_run_or_triplet(deck2[:idx]):
            return 2

        idx += 1

    return 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    arr = list(map(int, input().split()))

    deck1 = []
    deck2 = []
    for i in range(12):
        if i % 2:
            deck2.append(arr[i])
        else:
            deck1.append(arr[i])
    # 출력
    print(f"#{test_case} {solve()}")