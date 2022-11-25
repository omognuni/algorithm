import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

ds = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def recursive(y, x, d):
    global count

    if graph[y][x] == 0:
        count += 1
        graph[y][x] = 2

    endpoint = True

    for i in ds:
        tmp_x = x + i[1]
        tmp_y = y + i[0]

        if tmp_x < m and tmp_y < n and tmp_x >= 0 and tmp_y >= 0:
            if graph[tmp_y][tmp_x] == 0:
                endpoint = False
                break

    if endpoint:
        x -= ds[d][1]
        y -= ds[d][0]

        if graph[y][x] != 1:
            recursive(y, x, d)
        else:
            return

    else:
        # d -= 1
        # if d == -4:
        #     d = 0

        # 더 나은 방법
        d = (d+3) % 4

        new_x = x + ds[d][1]
        new_y = y + ds[d][0]

        if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n:
            if graph[new_y][new_x] == 0:
                recursive(new_y, new_x, d)

            else:
                recursive(y, x, d)


count = 0

recursive(r, c, d)
print(count)
