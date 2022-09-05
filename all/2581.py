'''
https://www.acmicpc.net/problem/2581
'''

import sys

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

m = int(input())
n = int(input())

sum = 0
min = n
for i in range(m, n+1):
    if is_prime(i):
        sum+=i
        if i <= min:
            min=i
if sum != 0:
    print(sum)
    print(min)
else:
    print(-1)