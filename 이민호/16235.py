# import sys
# from collections import deque
#
# n, m, k = map(int, sys.stdin.readline().split())
# board = [[5] * n for _ in range(n)]
# A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# tree_list = deque()
# for _ in range(m):
#     x, y, z = map(int, sys.stdin.readline().split())
#     x -= 1
#     y -= 1
#     tree_list.append([x, y, z])
#
# tree_list = sorted(tree_list, key=lambda x: x[2])
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
# for __ in range(k):
#     death = deque()
#     five = deque()
#     trees = deque()
#     for i in range(len(tree_list)):
#         if board[tree_list[i][0]][tree_list[i][1]] < tree_list[i][2]:
#             death.append(tree_list[i])
#         else:
#             board[tree_list[i][0]][tree_list[i][1]] -= tree_list[i][2]
#             tree_list[i][2] += 1
#             if tree_list[i][2] % 5 == 0:
#                 five.append(tree_list[i])
#             trees.append(tree_list[i])
#
#     for tree in death:
#         board[tree[1]][tree[0]] += (tree[2] // 2)
#     for tree in five:
#         for l in range(8):
#             nx, ny, = tree[0] + dx[l], tree[1] + dy[l]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             trees.append([nx, ny, 1])
#     tree_list = trees
#     for y in range(n):
#         for x in range(n):
#             board[y][x] += A[y][x]
# print(len(tree_list))
from collections import deque

n, m, k = map(int, input().split(' '))

a = [list(map(int, input().split(' '))) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_summer():
    for i in range(n):
        for j in range(n):
            len_ = len(trees[i][j])
            for k in range(len_):
                if graph[i][j] < trees[i][j][k]:
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2


def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)

            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
