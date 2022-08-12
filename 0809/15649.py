
import sys

input = sys.stdin.readline

s = []

n, m = map(int, input().split())


# 백트래킹
def dfs():

    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()


# 순열
# def p(arr, k):

#     result = []

#     if k > len(arr) + 1:
#         return

#     if k == 1:
#         for i in arr:
#             result.append([i])

#     if k > 1:
#         for i in range(len(arr)):
#             for j in p(arr[:i] + arr[i+1:], k-1):

#                 result.append([arr[i]] + j)

#     return result

# arr = [str(i) for i in range(1, n+1)]

# ans = p(arr, m)

# [print(" ".join(i)) for i in ans]
