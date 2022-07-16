import sys

input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a%b

    return a

def lcm(a,b):
    return int(a*b /gcd(a,b))

n = int(input())

ans = []
for i in range(n):
    a, b = map(int,input().split())
    ans.append(lcm(a,b))

[print(i) for i in ans]