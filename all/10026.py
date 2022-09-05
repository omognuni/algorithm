import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = []
blind_graph = []
visited = [[False for i in range(n)] for i in range(n)]

for i in range(n):
    g = list(map(str, input().strip('\n')))
    graph.append(g)

    new_g = deepcopy(g)
    for i in range(len(new_g)):
        if new_g[i] == 'G':
            new_g[i] = 'R'
    blind_graph.append(new_g)


def dfs(graph, start, visited):
    global n
    i = start[0]
    j = start[1]
    color = graph[i][j]

    if visited[i][j]:
        return

    visited[i][j] = True

    ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for d in ds:
        x = i + d[0]
        y = j + d[1]

        if x < 0 or x >= n or y < 0 or y >= n:
            continue

        if not visited[x][y] and color == graph[x][y]:
            dfs(graph, [x, y], visited)


ans = []
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            dfs(graph, [i, j], visited)

ans.append(count)

visited = [[False for i in range(n)] for i in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            dfs(blind_graph, [i, j], visited)

ans.append(count)

print(" ".join(map(str, ans)))
