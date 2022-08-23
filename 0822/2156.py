import sys
input = sys.stdin.readline

n = int(input())

d = [0 for i in range(n+100)]

q = [0]

for i in range(1, n+1):
    q.append(int(input()))

if n <= 1:
    d[1] = q[1]

else:
    d[1] = q[1]
    d[2] = q[1] + q[2]

    for i in range(3, n+1):
        d[i] = max(q[i] + q[i-1] + d[i-3], q[i] + d[i-2], d[i-1])


print(max(d))
