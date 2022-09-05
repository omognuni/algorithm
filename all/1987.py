import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for i in range(r):
    g = list(map(str, " ".join(input()).split()))
    graph.append(g)

ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
res = set()
ans = 0


def dfs(start, count):
    global ans
    ans = max(ans, count)

    for d in ds:
        x = start[0] + d[0]
        y = start[1] + d[1]

        if x < 0 or x >= r or y < 0 or y >= c:
            continue

        if graph[x][y] not in res:
            res.add(graph[x][y])
            count += 1
            dfs([x, y], count)
            res.remove(graph[x][y])
            count -= 1

    return


res.add(graph[0][0])
dfs([0, 0], 1)
print(ans)

# 첫 코드
# import sys

# input = sys.stdin.readline

# r, c = map(int, input().split())
# graph = []

# for i in range(r):
#     g = list(map(str, " ".join(input()).split()))
#     graph.append(g)
# visited = [[False for i in range(c)] for j in range(r)]

# ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# ans = 0


# def dfs(start, count, res, visited):
#     global ans

#     ans = max(ans, count)

#     for d in ds:
#         x = start[0] + d[0]
#         y = start[1] + d[1]

#         if x < 0 or x >= r or y < 0 or y >= c:
#             continue

#         if visited[x][y]:
#             continue

#         if graph[x][y] not in res and not visited[x][y]:
#             res.append(graph[x][y])
#             count += 1
#             visited[x][y] = True
#             dfs([x, y], count, res, visited)
#             res.pop()
#             count -= 1
#             visited[x][y] = False

#     return


# visited[0][0] = True

# dfs([0, 0], 1, [graph[0][0]], visited)

# print(ans)
