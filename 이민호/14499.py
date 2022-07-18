def dice_up(b, r):
    for i in range(1, 7):
        if r == i:
            d = dice_pattern[i - 1]
            if d.index(b) == 3:
                return d[0], i
            else:
                return d[d.index(b) + 1], i


def dice_down(b, r):
    for i in range(1, 7):
        if r == i:
            d = dice_pattern[i - 1]
            if d.index(b) == 0:
                return d[3], i
            else:
                return d[d.index(b) - 1], i


def dice_right(b, r):
    return r, 7 - b


def dice_left(b, r):
    return 7 - r, b


dice = [0, 0, 0, 0, 0, 0, 0]

dice_pattern = [[2, 4, 5, 3],
                [1, 3, 6, 4],
                [1, 5, 6, 2],
                [1, 2, 6, 5],
                [1, 4, 6, 3],
                [2, 3, 5, 4]]
n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice_b = 6
dice_r = 3
go = list(map(int, input().split()))
for k_i in range(k):
    if go[k_i] == 1:
        if not(0 <= x + 1 < m):
            continue
        x += 1
        dice_b, dice_r = dice_right(dice_b, dice_r)
    elif go[k_i] == 2:
        if not (0 <= x - 1 < m):
            continue
        x -= 1
        dice_b, dice_r = dice_left(dice_b, dice_r)
    elif go[k_i] == 3:
        if not (0 <= y - 1 < n):
            continue
        y -= 1
        dice_b, dice_r = dice_up(dice_b, dice_r)
    elif go[k_i] == 4:
        if not (0 <= y + 1 < n):
            continue
        y += 1
        dice_b, dice_r = dice_down(dice_b, dice_r)


    if board[y][x] == 0:
        board[y][x] = dice[dice_b]
    else:
        dice[dice_b] = board[y][x]
        board[y][x] = 0
    print(dice[7 - dice_b])
    #print(dice)
