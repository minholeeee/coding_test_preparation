n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#하나 잘못넣어서 두개 못넣을수도 있음
#넣을 수 있는 곳에 최대한 많이 넣기 안됨 진실하나때문에 헛개비 둘이..

#모든 경우의 수 생각하기 -> 너무 오래 걸리지만 가장 정확하긴 함
#아,, 지나갈깨마다 경사로를 넣는 느낌인가?-> 그렇데

can_go = 0
for x in range(n):
    up_stack = 1
    flag = True
    construction = 0
    for y in range(n - 1):
        if board[y][x] == board[y + 1][x]:
            up_stack += 1
        elif board[y][x] + 1 == board[y + 1][x]:
            if up_stack >= l:
                up_stack = 1
                if construction != 0 and construction >= y - l + 1:
                    flag = False
                    break
            else:
                flag = False
                break
        elif board[y][x] - 1 == board[y + 1][x]:
            up_stack = 1
            if y + l < n:
                flag2 = False
                for yy in range(y + 1, y + l + 1):
                    if board[y + 1][x] != board[yy][x]:
                        flag2 = True
                        break
                if flag2:
                    flag = False
                    break
            else:
                flag = False
                break
            construction = y + l
        else:
            flag = False
            break
    if flag:
        #print('x = ', x)
        can_go += 1

for y in range(n):
    up_stack = 1
    flag = True
    construction = 0
    for x in range(n - 1):
        if board[y][x] == board[y][x + 1]:
            up_stack += 1

        elif board[y][x] + 1 == board[y][x + 1]:
            if up_stack >= l:
                up_stack = 1
                if construction != 0 and construction >= x - l + 1:
                    flag = False
                    break
            else:
                flag = False
                break
        elif board[y][x] - 1 == board[y][x + 1]:
            up_stack = 1
            if x + l < n:
                check_set = set(board[y][x + 1:x + l + 1])
                if len(check_set) != 1:
                    flag = False
                    break
            else:
                flag = False
                break
            construction = l + x
        else:
            flag = False
            break
    if flag:
        #print('y = ', y)
        can_go += 1
print(can_go)
