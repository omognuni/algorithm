import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())

graph = []
start = []
count = 0


def is_finished(graph):
    finished = True

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                start.append([i, j])

            if graph[i][j] == 0:
                finished = False

    return finished


def bfs(graph, start):
    global m, n, count

    q = deque(start)
    new_q = deque([])

    ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:

        p = q.popleft()

        x = p[0]
        y = p[1]

        for d in ds:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                new_q.append([nx, ny])

        if not q:
            count += 1
            q = new_q
            new_q = deque([])

    return


for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

finished = is_finished(graph)

if finished:
    print(0)

else:
    bfs(graph, start)
    finished = is_finished(graph)

    if finished:
        # 마지막 다 채우면 큐가 0이여서 한번 더 카운트 되기 때문에 1 뺌
        print(count-1)

    else:
        print(-1)
