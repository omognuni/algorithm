import sys
from collections import deque
from copy import deepcopy
# pypy3 제출
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs():
    global answer
    tmp = deepcopy(graph)
    q = deque()

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append([i, j])

    while q:

        p = q.popleft()

        i = p[0]
        j = p[1]

        for i in range(4):

            x = i + ds[i][0]
            y = j + ds[i][1]

            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if tmp[x][y] == 0:
                tmp[x][y] = 2
                q.append([x, y])

    count = 0

    for i in range(n):
        count += tmp[i].count(0)

    answer = max(answer, count)
    return


def recursive(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                recursive(count + 1)
                graph[i][j] = 0


recursive(0)
print(answer)
