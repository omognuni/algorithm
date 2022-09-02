import sys
input = sys.stdin.readline
# 코테 고양이 문제


def combinations(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            if (i+1) in result:
                print('n')
                continue
            else:
                result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combinations(arr[i+1:], n-1):
                if (arr[i]+1) in j:
                    continue
                result.append([arr[i]] + j)

    return result


n = int(input())
_l = [i for i in range(1, n+1)]
ans = []
for i in range(len(_l)):
    if combinations(_l, i):
        ans += combinations(_l, i)

print(ans)
