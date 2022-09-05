import sys
import math
input = sys.stdin.readline

n = int(input())

ans = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            if r1 == 0:
                ans.append(1)
            if r1 != 0:
                ans.append(-1)
        if r1 != r2:
            ans.append(0)
        
    
    else:
        c_dist = math.sqrt(((x1-x2)**2 + (y1-y2)**2))
        dist = r1 + r2

        if c_dist > dist:
            ans.append(0)

        if c_dist == dist:
            ans.append(1)

        if c_dist < dist:
            if c_dist + r1 < r2 or c_dist + r2 < r1:
                ans.append(0)
                continue
            if c_dist + r1 == r2 or c_dist + r2 == r1:
                ans.append(1)
                continue
            else:
                ans.append(2)

[print(i) for i in ans]
