import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().strip('\n'))))

visited = [[0 for j in range(m)] for i in range(n)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]


q = deque([[0, 0]])
visited[0][0] = 1

while q:

    x, y = map(int, q.popleft())

    for i in range(len(d)):

        dx = x + d[i][0]
        dy = y + d[i][1]

        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue

        if visited[dx][dy] >= 1:
            continue

        if graph[dx][dy] == 1:
            visited[dx][dy] = visited[x][y] + 1
            q.append([dx, dy])

print(visited[n-1][m-1])
