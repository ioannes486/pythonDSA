path = []
result = 0
def recur(cnt):
    global result


    #기저 조건에서 많은 경우의 수를 줄일 수 있다.
    if sum(path) > 10:
        return

    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1
        return

    for num in range(1,6):
        path.append(num)
        recur(cnt+1)
        path.pop()


def recur2(cnt, total):
    global result

    # 기저 조건에서 많은 경우의 수를 줄일 수 있다.
    if total > 10:
        return

    if cnt == 3:
        if total <= 10:
            result += 1
        return

    for num in range(1, 7):
        total += num
        recur2(cnt + 1, total + num)

recur2(0, 0)
print(result)