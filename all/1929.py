'''
https://www.acmicpc.net/problem/1929
'''

import sys
import math
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False

    # 제곱근까지만 확인
    sq = int(math.sqrt(n))
    
    for i in range(2, sq+1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if is_prime(i):
        print(i)
