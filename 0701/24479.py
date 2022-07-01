
# 답이 간선 출력이 아니라 해당 간선이 몇번째로 방문했는지를 출력했어야 했다
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, start, visited, order):
    visited[start] = order

    for i in graph[start]:
        if visited[i] == 0:
            order = dfs(graph, i, visited, order + 1)
    
    return order

v, e, r = map(int, input().split())

visited = [0]*(v+1)

graph = [[] for i in range(v+1)]

order = 1

for i in range(1, e + 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    # 역방향 추가안함
    graph[end].append(start)



for i in range(1, v+1):
    graph[i].sort()

dfs(graph, r, visited, order)

for i in range(1,len(visited)):
    print(visited[i])