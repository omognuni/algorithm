import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

count = 0
# dp 로 풀기
# d = [0] * 2000001

# for i in data:
#     d[i] = 1

# for i in data:
#     if x - i > 0:
#         if d[x-i]:
#             count += 1

# print(count//2)

# 투 포인터로 풀기
data.sort()

start = 0
end = n - 1
total = 0


while start < end:

    total = data[start] + data[end]

    if total == x:
        count += 1

    elif total < x:
        start += 1
        continue
    end -= 1

print(count)
