from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

c = combinations(range(n), k )

res = 0
for i in c:
    res+=1

print(res)