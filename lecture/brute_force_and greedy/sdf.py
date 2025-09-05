path = []
used = [False for _ in range(3)]  # 인덱스 오류를 없애기 위해서 실제 고를 수 있는 수보다 1개 더 크게 만들어주기도 한다


def kfc(num):


    if num == 2:
        print(*path)
        return

    for num in range(3):
        # 이미 path에 있는 숫자는 생략
        if used[num]:   # in은 느리다 그래서 잘 안쓴다
            continue

        used[num] = True
        path.append(num)
        kfc(num + 1)
        path.pop()
        used[num] = False