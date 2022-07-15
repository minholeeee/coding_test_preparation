n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
#1. 할때마다 깊은 복사
#2. 그래도 어떻게 변수를 두기
import copy
stack = []
tmp_list = copy.deepcopy(board)
stack.append([tmp_list, 0])
def up(b):
    for x in range(n):
        tmp_stack = [b[0][x]]
        for y in range(1, n):
            if b[y][x] == 0:
                pass
            elif len(tmp_stack) > 0 and b[y][x] == tmp_stack[-1]:
                tmp_stack.append(tmp_stack.pop() * 2)
                tmp_stack.append(0)
                #합쳐진 녀석은 또합 합쳐지면 안됨
            else:
                tmp_stack.append(b[y][x])
        while 0 in tmp_stack:
            tmp_stack.remove(0)
        for t in range(n):
            if tmp_stack:
                b[t][x] = tmp_stack.pop(0)
            else:
                b[t][x] = 0
    return b
def down(b):
    for x in range(n):
        tmp_stack = [b[n-1][x]]
        for y in range(n - 2, -1, -1):
            if b[y][x] == 0:
                pass
            elif len(tmp_stack) > 0 and b[y][x] == tmp_stack[-1]:
                tmp_stack.append(tmp_stack.pop() * 2)
                tmp_stack.append(0)
            else:
                tmp_stack.append(b[y][x])
        while 0 in tmp_stack:
            tmp_stack.remove(0)
        for t in range(n-1, -1, -1):
            if tmp_stack:
                b[t][x] = tmp_stack.pop(0)
            else:
                b[t][x] = 0
    return b
def left(b):
    for y in range(n):
        tmp_stack = [b[y][0]]
        for x in range(1, n):
            if b[y][x] == 0:
                pass
            elif len(tmp_stack) > 0 and b[y][x] == tmp_stack[-1]:
                tmp_stack.append(tmp_stack.pop() * 2)
                tmp_stack.append(0)
            else:
                tmp_stack.append(b[y][x])
        while 0 in tmp_stack:
            tmp_stack.remove(0)
        for t in range(n):
            if tmp_stack:
                b[y][t] = tmp_stack.pop(0)
            else:
                b[y][t] = 0
    return b
def right(b):
    for y in range(n):
        tmp_stack = [b[y][n-1]]
        for x in range(n - 2, -1, -1):
            if b[y][x] == 0:
                pass
            elif len(tmp_stack) > 0 and b[y][x] == tmp_stack[-1]:
                tmp_stack.append(tmp_stack.pop() * 2)
                tmp_stack.append(0)
            else:
                tmp_stack.append(b[y][x])
        while 0 in tmp_stack:
            tmp_stack.remove(0)
        for t in range(n - 1, -1, -1):
            if tmp_stack:
                b[y][t] = tmp_stack.pop(0)
            else:
                b[y][t] = 0
    return b
# 스택에 넣을 때 깊은 복사를 하자
max_b = 0
while stack:
    now_list, now = stack.pop(0)
    ul = copy.deepcopy(now_list)
    if now < 5:
        stack.append([up(ul), now + 1])
    else:
        for i in range(n):
            if max_b < max(ul[i]):
                max_b = max(ul[i])
    dl = copy.deepcopy(now_list)
    if now < 5:
        stack.append([down(dl), now + 1])
    else:
        for i in range(n):
            if max_b < max(ul[i]):
                max_b = max(ul[i])
    rl = copy.deepcopy(now_list)
    if now < 5:
        stack.append([right(rl), now + 1])
    else:
        for i in range(n):
            if max_b < max(ul[i]):
                max_b = max(ul[i])
    ll = copy.deepcopy(now_list)
    if now < 5:
        stack.append([left(ll), now + 1])
    else:
        for i in range(n):
            if max_b < max(ul[i]):
                max_b = max(ul[i])
print(max_b)

