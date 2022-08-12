'''
https://www.acmicpc.net/problem/2751
'''

import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

# nums = sorted(nums)
# print("\n".join(str(i) for i in nums))

# '''
# 내장함수 안쓰고 퀵정렬 구현하기
# '''


def quicksort(nums, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and nums[left] <= nums[pivot]:
            left += 1
        
        while right > start and nums[right] >= nums[pivot]:
            right -= 1

        if left <= right:
            nums[right], nums[left] = nums[left], nums[right]
        else:
            nums[right], nums[pivot] = nums[pivot], nums[right]

    quicksort(nums, pivot, right - 1)
    quicksort(nums, right + 1, end)

quicksort(nums, 0, len(nums) - 1)
print("\n".join(str(i) for i in nums))