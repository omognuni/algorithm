'''
하노이탑
https://www.acmicpc.net/problem/11729
'''

import sys
input = sys.stdin.readline


def recursive(n, a, b, c):
    if n == 1:
        print(a, c)

    else:
        recursive(n-1, a, c, b)
        print(a, c)
        recursive(n-1, b, a, c)


n = int(input())
print(2**n-1)
recursive(n, 1, 2, 3)
