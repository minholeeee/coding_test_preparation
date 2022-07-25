import copy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def make_dragon(stack):
    new_stack = []
    tmp_stack = copy.deepcopy(stack)
    s_x, s_y, w = tmp_stack[-1]
    new_stack.append([s_x, s_y, w])
    for _ in stack:
        t_x, t_y, w = tmp_stack.pop()
        s_x += dx[new_stack[-1][2] % 4]
        s_y += dy[new_stack[-1][2] % 4]
        w += 1
        new_stack.append([s_x, s_y, w])
    new_stack.pop(0)
    return stack + new_stack

n = int(input())
def check_sq(xys):
    re = 0
    for xy in xys:
        if (xy[0] + 1, xy[1]) in xys and (xy[0] + 1, xy[1] + 1) in xys and (xy[0], xy[1] + 1) in xys:
            re += 1
    return re
all_s = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    d_stack = []
    d_stack.append([x, y, d])
    for deep in range(g):
        d_stack = make_dragon(d_stack)
    for d in d_stack:
        all_s.append((d[0], d[1]))
    all_s.append((d_stack[-1][0] + dx[d_stack[-1][2] % 4], d_stack[-1][1] + dy[d_stack[-1][2] % 4]))
all_s = set(all_s)
print(check_sq(all_s))
