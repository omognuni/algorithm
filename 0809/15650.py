
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 백트래킹
s = []


def dfs(start):

    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


dfs(1)
# 조합
# def c(arr, k):

#     result = []

#     if k > len(arr) + 1:
#         return

#     if k == 1:
#         for i in arr:
#             result.append([i])

#     elif k > 1:
#         for i in range(len(arr) - k + 1):
#             for j in c(arr[i+1:], k-1):
#                 result.append([arr[i]] + j)

#     return result


# arr = [str(i) for i in range(1, n+1)]

# ans = c(arr, m)

# [print(" ".join(i)) for i in ans]
