import sys
sys.stdin = open("input.txt", "r")

"""TODO:
- 상수

- 변수

- 조건(제약사항)

- 구하는 값

- 아이디어
"""

def solve(lst1, lst2):
    # 카운팅 정렬 만들기
    cnt_arr1 = [0]* 123
    cnt_arr2 = [0]* 123

    # 비교대상이 될 리스트의 카운팅 정렬 구하기
    for i in range(len(lst1)):
        cnt_arr1[lst1[i]] += 1

    for j in range(len(lst2)):
        cnt_arr2[lst2[j]] += 1

    max_number = 0
    for k in range(123):
        # 두 열에 모두 존재함
        if cnt_arr1[k] and cnt_arr2[k]:
            if max_number < cnt_arr2[k]:
                max_number = cnt_arr2[k]


    return max_number


T = int(input())
for test_case in range(1, T + 1):
    # 입력
    str1 = input()
    str2 = input()

    lst1 = []
    lst2 = []
    for char in str1:
        lst1.append(ord(char))

    for char in str2:
        lst2.append(ord(char))


    # 출력
    print(f"#{test_case} {solve(lst1, lst2)}")