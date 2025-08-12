def solve(total_page, A_target_page, B_target_page):
    l = 1
    r = total_page
    middle = (l+r) // 2

    # 먼저 구하기
    A_count = 0
    while middle != A_target_page:
        middle = (l + r) // 2
        if middle == A_target_page:
            break
        elif middle > A_target_page:
            r = middle
            A_count += 1
        elif middle < A_target_page:
            l = middle
            A_count += 1

    l = 1
    r = total_page
    middle = (l + r) // 2

    B_count = 0
    while middle != B_target_page:
        middle = (l + r) // 2
        if middle == B_target_page:
            break
        elif middle > B_target_page:
            r = middle
            B_count += 1
        elif middle < B_target_page:
            l = middle
            B_count += 1

    if A_count < B_count:
        return "A"
    elif A_count == B_count:
        return "0"
    return "B"


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    total_page, A_target_page, B_target_page = map(int, input().split())

    # 출력
    print(f"#{test_case} {solve(total_page, A_target_page, B_target_page)}")