import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())


def recursive(n, r, c):
    if n == 0:
        return 0
    half = 2**(n-1)
    if r < half and c < half:
        return recursive(n-1, r, c)
    elif r < half and c >= half:
        return half*half + recursive(n-1, r, c - half)
    elif r >= half and c < half:
        return 2*half*half + recursive(n-1, r - half, c)
    elif r >= half and c >= half:
        return 3*half*half + recursive(n-1, r - half, c - half)


answer = recursive(n, r, c)

print(answer)
