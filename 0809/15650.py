# 조합
import sys

input = sys.stdin.readline


def c(arr, k):

    result = []

    if k > len(arr) + 1:
        return

    if k == 1:
        for i in arr:
            result.append([i])

    elif k > 1:
        for i in range(len(arr) - k + 1):
            for j in c(arr[i+1:], k-1):
                result.append([arr[i]] + j)

    return result


n, m = map(int, input().split())


arr = [str(i) for i in range(1, n+1)]

ans = c(arr, m)

[print(" ".join(i)) for i in ans]
