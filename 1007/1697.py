import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1 for i in range(100001)]
visited[n] = 0

q = deque([n])

while q:
    x = q.popleft()

    d = [x-1, x+1, x*2]

    for i in range(len(d)):
        if d[i] > 100000 or d[i] < 0:
            continue

        if visited[d[i]] >= 0:
            continue

        visited[d[i]] = visited[x] + 1
        q.append(d[i])

print(visited[k])
