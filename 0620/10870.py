'''
https://www.acmicpc.net/problem/10870
'''
import sys

input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))