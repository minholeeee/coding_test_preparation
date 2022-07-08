n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
day = 0
from collections import OrderedDict

while (True):
    _unions = []
    end_flag = True
    for y in range(n):
        for x in range(n):
            if y >= 1:
                if l <= abs(a[y][x] - a[y - 1][x]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y - 1, x])
                            flag = True
                        elif [y - 1, x] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y - 1, x]])
            if y + 1 < n:
                if l <= abs(a[y][x] - a[y + 1][x]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y + 1, x])
                            flag = True
                        elif [y + 1, x] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        tmp = [[y, x], [y + 1, x]]
                        _unions.append(tmp)
            if x >= 1:
                if l <= abs(a[y][x] - a[y][x - 1]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y, x - 1])
                            flag = True
                        elif [y, x - 1] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y, x - 1]])
            if x + 1 < n:
                if l <= abs(a[y][x] - a[y][x + 1]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y, x + 1])
                            flag = True
                        elif [y, x + 1] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y, x + 1]])
    if end_flag:
        break
    day += 1
    for _union in _unions:
        real_union = []
        real_union = list(OrderedDict.fromkeys(_union))
        sum_uni = 0
        for con in real_union:
            sum_uni += a[con[0]][con[1]]
        sum_uni //= len(real_union)
        for con in real_union:
            a[con[0]][con[1]] = sum_uni

print(day)

# n, l, r = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# graph = [[0 for _ in range(n**2)] for __ in range(n**2)]
# days = 0
# while (True):
#     flag = True
#     for y in range(n):
#         for x in range(n):
#             if y >= 1:
#                 if l <= abs(a[y][x] - a[y - 1][x]) <= r:
#                     flag = False
#                     graph[n * y + x][n * (y - 1) + x] = 1
#                     graph[n * (y - 1) + x][n * y + x] = 1
#
#             if y + 1 < n:
#                 if l <= abs(a[y][x] - a[y + 1][x]) <= r:
#                     flag = False
#
#             if x >= 1:
#                 if l <= abs(a[y][x] - a[y][x - 1]) <= r:
#                     flag = False
#
#             if x + 1 < n:
#                 if l <= abs(a[y][x] - a[y][x + 1]) <= r:
#                     flag = False
#     if flag:
#         break
#     days += 1
n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
day = 0
from collections import OrderedDict

while (True):
    _unions = []
    end_flag = True
    for y in range(n):
        for x in range(n):
            if y >= 1:
                if l <= abs(a[y][x] - a[y - 1][x]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y - 1, x])
                            flag = True
                        elif [y - 1, x] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y - 1, x]])
            if y + 1 < n:
                if l <= abs(a[y][x] - a[y + 1][x]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y + 1, x])
                            flag = True
                        elif [y + 1, x] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        tmp = [[y, x], [y + 1, x]]
                        _unions.append(tmp)
            if x >= 1:
                if l <= abs(a[y][x] - a[y][x - 1]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y, x - 1])
                            flag = True
                        elif [y, x - 1] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y, x - 1]])
            if x + 1 < n:
                if l <= abs(a[y][x] - a[y][x + 1]) <= r:
                    flag = False
                    end_flag = False
                    for _union in _unions:
                        if [y, x] in _union:
                            _union.append([y, x + 1])
                            flag = True
                        elif [y, x + 1] in _union:
                            _union.append([y, x])
                            flag = True
                    if not flag:
                        _unions.append([[y, x], [y, x + 1]])
    if end_flag:
        break
    day += 1
    for _union in _unions:
        real_union = list(set(map(tuple, _union)))
        sum_uni = 0
        for con in real_union:
            sum_uni += a[con[0]][con[1]]
        sum_uni //= len(real_union)
        for con in real_union:
            a[con[0]][con[1]] = sum_uni

print(day)
