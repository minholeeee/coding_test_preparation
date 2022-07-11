c_num = int(input())
l_num = int(input())
graph = [[] for _ in range(c_num)]
visited = [0] * c_num
for _ in range(l_num):
    san1, san2 = map(int, input().split())
    san1 -= 1
    san2 -= 1
    graph[san1].append(san2)
    graph[san2].append(san1)
com = []

def dfs(start):
    if visited[start] == 1:
        return
    visited[start] = 1
    for g in graph[start]:
        dfs(g)
dfs(0)
print(visited.count(1) - 1)
