import sys

sys.stdin = open("../swea_5432_쇠막대자르기/input.txt", "r")


def solve(text):
    stack = []
    total_count = 0

    i = 0
    text_length = len(text)
    while i < text_length:
        char = text[i]

        if char == "(":
            stack.append(char)

        else:
            stack.pop()

            if i > 0 and text[i - 1] == "(":
                total_count += len(stack)
            else:
                total_count += 1
        i += 1

    return total_count


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    input_text = input()
    # 출력
    print(f"#{test_case} {solve(input_text)}")
