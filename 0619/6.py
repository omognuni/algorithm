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



