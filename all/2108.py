import sys
input = sys.stdin.readline

n = int(input())

tmp = [0 for i in range(8001)]

nums = []
for i in range(n):
    nums.append(int(input()))

sum = 0
for i in range(n):
    sum += nums[i]
    tmp[nums[i]] += 1

ans = []
max_idx = 0
for i in range(len(tmp)):
    if tmp[i] == 0:
        continue
    if tmp[max_idx] == tmp[i]:
        ans.append(i)

    if tmp[max_idx] < tmp[i]:
        max_idx = i
        ans = []

ans.append(max_idx)

for i in range(len(ans)):
    if ans[i] > 4000:
        ans[i] -= 8001
ans.sort()

print(round(sum/n))

nums.sort()
print(nums[n//2])

if len(ans) > 1:
    print(ans[1])
else:
    print(ans[0])

print(max(nums)-min(nums))
