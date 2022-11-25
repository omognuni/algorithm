import sys
from collections import deque
input = sys.stdin.readline


def solution():
    r, c = map(int, input().split())
    graph = []
    visited1 = [[-1 for i in range(c)] for j in range(r)]
    visited2 = [[-1 for i in range(c)] for j in range(r)]
    q1 = deque([])
    q2 = deque([])

    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(r):
        graph.append(list(map(str, input().strip('\n'))))

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                visited1[i][j] = 0
                q1.append([i, j])
            if graph[i][j] == 'J':
                visited2[i][j] = 0
                q2.append([i, j])

    while q1:
        x, y = map(int, q1.popleft())

        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]

            if dx < 0 or dy < 0 or dx >= r or dy >= c:
                continue

            if visited1[dx][dy] >= 0 or graph[dx][dy] == '#':
                continue

            visited1[dx][dy] = visited1[x][y] + 1
            q1.append([dx, dy])

    while q2:
        x, y = map(int, q2.popleft())

        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]

            if dx < 0 or dy < 0 or dx >= r or dy >= c:
                print(visited2[x][y] + 1)
                return

            if visited2[dx][dy] >= 0 or graph[dx][dy] == '#':
                continue

            if visited1[dx][dy] != -1 and visited1[dx][dy] <= visited2[x][y] + 1:
                continue

            visited2[dx][dy] = visited2[x][y] + 1
            q2.append([dx, dy])

    print('IMPOSSIBLE')


solution()
# for i in range(r):
#     for j in range(c):
#         if graph[i][j] == 'J':
#             start.append([i, j])
#             j_visited[i][j] = 0

#         if graph[i][j] == 'F':
#             fires.append([i, j])
#             fire_visited[i][j] = 0

#         if graph[i][j] != '#' and (i == r-1 or j == c-1 or i == 0 or j == 0):
#             esc.append([i, j])

# def bfs(xy, visited):
#     global r, c
#     q = deque(xy)

#     while q:
#         x, y = map(int, q.popleft())

#         for i in range(len(d)):
#             dx = x + d[i][0]
#             dy = y + d[i][1]

#             if dx < 0 or dy < 0 or dx >= r or dy >= c:
#                 continue

#             if visited[dx][dy] >= 0:
#                 continue

#             if graph[dx][dy] == '#':
#                 continue

#             if graph[dx][dy] == '.':
#                 visited[dx][dy] = visited[x][y] + 1
#                 q.append([dx, dy])

# bfs(start, j_visited)

# if fires:
#     bfs(fires, fire_visited)

# res = []

# for p in esc:
#     if j_visited[p[0]][p[1]] >= 0:
#         if fire_visited[p[0]][p[1]] == -1:
#             res.append(j_visited[p[0]][p[1]])

#         if j_visited[p[0]][p[1]] < fire_visited[p[0]][p[1]]:
#             res.append(j_visited[p[0]][p[1]])

# if res and start:
#     print(min(res) + 1)

# else:
#     print('IMPOSSIBLE')
