def make_set(x):



def find_set(x):

    if x == parents[x]:
        return x

    return find_set(parents[x])

def union(x):
    rep_x = find_set(x)
    rep_y = find_set(y)


    if rep_x == rep_y:
        return

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents
    parents[rep_x] = rep_x

N = 6
parents = make_set(N)
