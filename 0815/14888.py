import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
ans = []


def calc(a, b, i):
    if i == 0:
        return a + b
    if i == 1:
        return a - b
    if i == 2:
        return a * b
    if i == 3:
        if a < 0 and b > 0:
            a = -a
            return -(a//b)
        return a // b


def dfs(start, total, op_count):
    res = 0
    if op_count == op:
        ans.append(total)
        return

    for i in range(start + 1, len(nums)):
        for j in range(4):
            if op_count[j] == op[j]:
                continue
            op_count[j] += 1
            res = calc(total, nums[i], j)
            dfs(i, res, op_count)
            res = total
            op_count[j] -= 1


op_count = [0, 0, 0, 0]
dfs(0, nums[0], op_count)
print(max(ans), min(ans))
