import sys
input = sys.stdin.readline

n, c = map(int, input().split())

xs = []
for i in range(n):
    xs.append(int(input()))

xs.sort()


def binary(arr, start, end):
    global ans, c

    while start <= end:
        count = 1
        mid = (start + end) // 2
        now = arr[0]

        for i in range(len(arr)):
            if arr[i] >= now + mid:
                count += 1
                now = arr[i]

        if count >= c:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return


start = 1
end = xs[-1] - xs[0]
ans = 0

binary(xs, start, end)
print(ans)
