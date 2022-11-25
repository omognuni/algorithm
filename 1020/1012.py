import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(t):

    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    starts = []

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        starts.append([x, y])

    for start in starts:
        i = start[1]
        j = start[0]

        if graph[i][j] == 1:

            q = deque([[i, j]])
            graph[i][j] = 0

            while q:

                x1, y1 = q.popleft()

                for k in range(len(d)):
                    dx = x1 + d[k][0]
                    dy = y1 + d[k][1]

                    if dx < 0 or dy < 0 or dx >= n or dy >= m:
                        continue

                    if graph[dx][dy] == 0:
                        continue

                    if graph[dx][dy] == 1:
                        graph[dx][dy] = 0
                        q.append([dx, dy])

            cnt += 1

    print(cnt)
