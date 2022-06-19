import sys
input = sys.stdin.readline

d = [[] for i in range(15)]
d[0] = [i for i in range(1, 15)]

for i in range(1, len(d)):
    sum = 0
    for j in range(len(d[i-1])):
        sum += d[i-1][j]
        d[i].append(sum)

T = int(input())
ks = []
ns = []
for i in range(T):
    k = int(input())
    n = int(input())
    ks.append(k)
    ns.append(n)

for i in range(T):
    print(d[ks[i]][ns[i]-1])
