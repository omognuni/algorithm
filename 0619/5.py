import sys
import math
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False

    sq = int(math.sqrt(n))
    
    for i in range(2, sq+1):
        if n % i == 0:
            return False
    return True

case = []

while True:
    k = int(input())
    if k == 0:
        break
    else:
        case.append(k)

primes = []
# 문제에 제한된 범위 내에서 모든 소수를 구함
for i in range(1, 123456*2+1):
    if is_prime(i):
        primes.append(i)

for n in case:
    count = 0
    for i in primes:
        if n < i < 2*n+1:
            count+=1

    print(count)

