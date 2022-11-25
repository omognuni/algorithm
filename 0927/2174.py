import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

r_loc = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # N E S W
graph = [[0 for i in range(a)] for i in range(b)]
ans = ''

for i in range(n):
    x, y, d = input().split()
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    elif d == 'W':
        d = 3
    x = int(x) - 1
    y = int(y) - 1
    r_loc.append([x, y, d])
    graph[y][x] = i + 1

for i in range(m):

    idx, command, time = input().split()
    idx = int(idx)
    time = int(time)
    nd = r_loc[idx-1][2]

    if ans:
        continue

    for _ in range(time):
        if ans:
            continue

        if command == 'L':
            nd = (nd - 1) % 4

        elif command == 'R':
            nd = (nd + 1) % 4

        elif command == 'F':
            nx = r_loc[idx-1][0]
            ny = r_loc[idx-1][1]

            x = nx + directions[nd][1]
            y = ny + directions[nd][0]

            if x < 0 or y < 0 or x >= a or y >= b:
                ans = f"Robot {idx} crashes into the wall"

            else:
                if graph[y][x] != 0:
                    ans = f"Robot {idx} crashes into robot {graph[y][x]}"
                else:
                    graph[y][x] = idx
                    graph[ny][nx] = 0
                    r_loc[idx-1][0] = x
                    r_loc[idx-1][1] = y

        r_loc[idx-1][2] = nd


if not ans:
    ans = 'OK'

print(ans)
