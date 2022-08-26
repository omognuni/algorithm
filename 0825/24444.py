import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0 for i in range(n+1)]

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

order = 1


def bfs(graph, start, visited, order):

    visited[start] = order
    q = [start]
    q = deque(q)

    while q:
        # pop이 아니라 popleft
        u = q.popleft()
        graph[u].sort()
        for i in graph[u]:
            if not visited[i]:
                order += 1
                visited[i] = order
                q.append(i)

    return order


bfs(graph, r, visited, order)

[print(visited[i]) for i in range(1, n+1)]
