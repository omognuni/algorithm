import sys

# 파이썬으로 풀면 시간초과난다..
input = sys.stdin.readline
n = int(input())
row = [0] * n
c = 0
res = []
v = [False for _ in range(n)]
def is_safe(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
def dfs(x):
    global c
    if x == n:
        c += 1
        return
    for i in range(n):
        if v[i]:
            continue
        row[x] = i

        if is_safe(x):
            v[i] = True
            dfs(x+1)
            v[i] = False
dfs(0)
print(c)