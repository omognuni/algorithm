'''
https://www.acmicpc.net/problem/7568
'''
import sys
input = sys.stdin.readline

n = int(input())

specs = []
for i in range(n):
    x, y = map(int, input().split())
    specs.append([x, y, 1])

for i in range(len(specs)-1):
    for j in range(i, len(specs)):
        if specs[i][0] > specs[j][0] and specs[i][1] > specs[j][1]:
            specs[j][2] += 1
        if specs[i][0] < specs[j][0] and specs[i][1] < specs[j][1]:
            specs[i][2] += 1
        else:
            continue

print(" ".join([str(specs[i][2]) for i in range(len(specs))]))
