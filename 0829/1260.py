import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

dfs_res = []
bfs_res = []


def dfs(graph, start, visited):
    if visited[start]:
        return
    dfs_res.append(start)
    visited[start] = True

    graph[start].sort()

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

    return


def bfs(graph, start, visited):

    visited[start] = True

    q = deque([start])

    while q:

        x = q.popleft()

        bfs_res.append(x)

        graph[x].sort()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


dfs_v = [False] * (n+1)
bfs_v = [False] * (n+1)
dfs(graph, v, dfs_v)


bfs(graph, v, bfs_v)

print(" ".join(map(str, dfs_res)))
print(" ".join(map(str, bfs_res)))
