import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
stacks = []

ans = []

for i in range(n):
    hq.heappush(stacks, int(input()))


if len(stacks) < 2:
    # 카드 덱 1개이면 비교 안하니까 0이다
    print(0)

else:
    total = 0

    while len(stacks) >= 2:
        if len(stacks) >= 2:
            a = hq.heappop(stacks)
            b = hq.heappop(stacks)
            total = a + b
            ans.append(total)
            hq.heappush(stacks, total)
        
        else:
            c = hq.heappop(stacks)
            total = c + stacks[0]
            ans.append(total)

    print(sum(ans))

