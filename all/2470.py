import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

start = 0
end = n-1
min_value = 2000000001
ans = []

while start < end:

    temp = abs(data[start] + data[end])

    if temp < min_value:
        min_value = temp
        ans.append(data[start])
        ans.append(data[end])
        if abs(data[start]) < abs(data[end]):
            start += 1
        else:
            end -= 1
        continue

    if abs(data[start]) > abs(data[end]):
        start += 1
        continue

    end -= 1

print(" ".join(map(str, ans)))
