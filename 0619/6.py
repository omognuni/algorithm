'''
https://www.acmicpc.net/problem/9020
'''

import sys
import math
from collections import deque
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False

    sq = int(math.sqrt(n))

    for i in range(2, sq+1):
        if n % i == 0:
            return False
    return True


t = int(input())

case = []

for i in range(t):
    case.append(int(input()))

all_primes = []

for i in range(1, 10001):
    if is_prime(i):
        all_primes.append(i)


for num in case:
    for i in range(num//2, 1, -1):
        if i in all_primes and num-i in all_primes:
            print(i, num-i)
            break

# 큰 수부터 시작해서 break 문으로 나가야 했다
# for num in case:
#     ans = deque()
#     for i in range(2, num//2+1):
#         if i in all_primes and num-i in all_primes:
#             if ans:
#                 a, b = ans.pop()
#                 if abs(a-b) > abs(num-i-i):
#                     ans.append([i, num-i])
#                 else:
#                     ans.append([a, b])
#             else:
#                 ans.append([i, num-i])

#     print(ans[0][0], ans[0][1])
