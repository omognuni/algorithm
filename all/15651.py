import sys

input = sys.stdin.readline


def p(arr, k):

    result = []

    if k > len(arr) + 1:
        return

    if k == 1:
        for i in arr:
            result.append([i])

    if k > 1:
        for i in range(len(arr)):
            for j in p(arr, k-1):
                result.append([arr[i]] + j)

    return result


n, m = map(int, input().split())


arr = [str(i) for i in range(1, n+1)]

ans = p(arr, m)

[print(" ".join(i)) for i in ans]
