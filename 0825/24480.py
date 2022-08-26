import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

visited = [0 for i in range(n+1)]

graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

order = 1


def dfs(graph, start, visited, order):
    if visited[start] != 0:
        return

    visited[start] = order

    graph[start] = sorted(graph[start], reverse=True)
    for i in graph[start]:
        if visited[i] == 0:
            order = dfs(graph, i, visited, order + 1)

    return order


dfs(graph, r, visited, order)
for i in range(1, len(visited)):
    print(visited[i])
