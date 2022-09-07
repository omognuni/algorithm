import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

n = int(input())
ans = []
for i in range(n):
    line = input().split()

    if len(line) == 2:
        cmd = line[0]
        num = line[1]

    else:
        cmd = line[0]

    if cmd == 'push':
        q.append(num)

    if cmd == 'pop':
        if q:
            tmp = q.popleft()
            ans.append(tmp)
        else:
            ans.append(-1)
    
    if cmd == 'size':
        ans.append(len(q))
    
    if cmd == 'empty':
        if q:
            ans.append(0)
        else:
            ans.append(1)

    if cmd == 'front':
        if q:
            ans.append(q[0])
        else:
            ans.append(-1)
    if cmd == 'back':
        if q:
            ans.append(q[-1])
        else:
            ans.append(-1)

[print(i) for i in ans]
