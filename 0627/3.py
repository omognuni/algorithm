'''
https://www.acmicpc.net/problem/1018
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chess = [[] for i in range(m)]

for i in range(m):
    l = list(input().strip('\n'))
    chess[i].append(l)


for i in range(n):
    for j in range(m):
