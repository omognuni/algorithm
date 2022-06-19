'''
https://www.acmicpc.net/problem/1193
'''

import sys
input = sys.stdin.readline

k = int(input())

i=0
while k>0:
    i += 1
    k -= i

if i % 2 == 0:
    print(f'{i+k}/{1-k}')
else:
    print(f'{1-k}/{i+k}')
