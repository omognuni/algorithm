'''
https://www.acmicpc.net/problem/1978
'''
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

k = int(input())

n = map(int, input().split())

count = 0
for i in n:
    if is_prime(i):
        count += 1

print(count)