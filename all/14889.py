import sys
input = sys.stdin.readline

n = int(input())

players = []
players_num = [i for i in range(n)]

for i in range(n):
    players.append(list(map(int, input().split())))

t1 = []
t2 = []
res = 1000


def dfs(start):
    global res

    if len(t1) == n//2:
        t2 = list(set(players_num) - set(t1))
        total_1 = 0
        total_2 = 0
        for i in range(len(t1)):
            for j in range(len(t1)):
                total_1 += players[t1[i]][t1[j]]
                total_2 += players[t2[i]][t2[j]]

        if abs(total_1 - total_2) <= res:
            res = abs(total_1 - total_2)
        return

    for i in range(start, n):
        if i in t1:
            continue
        t1.append(i)
        dfs(i+1)
        t1.pop()


dfs(0)
print(res)
