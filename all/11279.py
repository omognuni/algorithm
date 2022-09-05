import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())

heap = []

ans = []
for i in range(n):
    x = int(input())

    if x == 0:
        if heap:
            ans.append(hq.heappop(heap)[1])
        else:
            ans.append(0)

    else:
        hq.heappush(heap, (abs(x), x))

[print(i) for i in ans]
