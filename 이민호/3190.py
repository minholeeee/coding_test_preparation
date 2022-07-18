n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
snake_way = []
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
l = int(input())
for _ in range(l):
    x, c = input().split()
    X = int(x)
    snake_way.append([X, c])
sec = 0
snake_head = [0, 0, 0]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake_body = []
snake_body.append([0, 0])
while True:
    if snake_way and snake_way[0][0] == sec:
        if snake_way[0][1] == 'D':
            snake_head[2] += 1
        elif snake_way[0][1] == 'L':
            snake_head[2] -= 1
        snake_way.pop(0)
        if snake_head[2] < 0:
            snake_head[2] += 4
        elif snake_head[2] >= 4:
            snake_head[2] -= 4
    sec += 1
    if not(0 <= snake_head[0] + dy[snake_head[2]] < n and 0 <= snake_head[1] + dx[snake_head[2]] < n):
        break
    snake_head[0] += dy[snake_head[2]]
    snake_head[1] += dx[snake_head[2]]

    if board[snake_head[0]][snake_head[1]] == 2:
        break
    snake_body.append([snake_head[0], snake_head[1]])

    if board[snake_head[0]][snake_head[1]] != 1:
        sy, sx = snake_body.pop(0)
        board[sy][sx] = 0
    board[snake_head[0]][snake_head[1]] = 2
print(sec)
