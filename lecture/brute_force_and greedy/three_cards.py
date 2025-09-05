cards = ['A', 'J','Q','K']
path = []
result = 0

# 연속된 3개가 나오면 return true, 아니면 false

def count_three():

    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(cnt):
    global result
    if cnt == 5:
        # todo : 연속된 3개가 나오면 세기
        if count_three():
            result += 1
            print(*path)

        return

    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt+1)
        path.pop()
recur(0)
print(result)
