import math

T = int(input())

ans = []
for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    ans.append(bridge)

[print(i) for i in ans]
