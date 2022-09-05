'''
https://www.acmicpc.net/problem/2750
'''
import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))


for i in range(len(nums)):
    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[min_idx] > nums[j]:
            nums[min_idx], nums[j] = nums[j], nums[min_idx]

print("\n".join(str(i) for i in nums))