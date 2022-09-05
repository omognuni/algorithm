import sys
input = sys.stdin.readline

n = int(input())

d = [0 for i in range(n+1)]

scores = [0]

for i in range(n):
    score = int(input())
    scores.append(score)

if n <= 2:
    print(sum(scores))

else:
    d[0] = 0
    d[1] = scores[1]
    d[2] = scores[1] + scores[2]

    for i in range(3, n + 1):

        d[i] = max(scores[i] + scores[i-1] + d[i-3], d[i-2] + scores[i])

    print(d[-1])
