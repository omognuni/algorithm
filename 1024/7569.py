import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
d = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
graphs = []
q = deque([])
finished = True

for i in range(h):
    graph = []
    for j in range(n):
        tmp = list(map(int,input().split()))
        for k in range(m):
            if tmp[k] == 1:
                q.append([i,j,k])
            
            if tmp[k] == 0:
                finished = False
        graph.append(tmp)
    graphs.append(graph)

if finished:
    print(0)

else:
    count = 0

    while q:
        
        z,y,x  = q.popleft()
        
        for i in range(6):
            dx = x + d[i][2]
            dy = y + d[i][1]
            dz = z + d[i][0]
            
            if dx < 0 or dy < 0 or dz < 0 or dx>=m or dy>=n or dz>=h:
                continue
            
            if graphs[dz][dy][dx] == 0:
                graphs[dz][dy][dx] = graphs[z][y][x] + 1
                q.append([dz, dy, dx])
            


    for i in range(h):
        for j in range(n):
            for k in range(m):
                count = max(count, graphs[i][j][k])
                if graphs[i][j][k] == 0:
                    print(-1)
                    exit(0)

    print(count-1)
