for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


def kfc(num):


    if num == 2:
        print(*path)
        return

    for num in range(3):
        path.append(num)
        kfc(num + 1)
        path.pop()





path = []
print('끝')
kfc(0)