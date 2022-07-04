import sys
input = sys.stdin.readline

n = list(input().strip('\n'))
n = [int(i) for i in n]
new = sorted(n, reverse=True)

[print(i, end='') for i in new]
