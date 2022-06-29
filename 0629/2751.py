'''
https://www.acmicpc.net/problem/2751
'''

import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

nums = sorted(nums)
print("\n".join(str(i) for i in nums))

# '''
# 내장함수 안쓰고 퀵정렬 구현하기
# '''


# def quicksort(nums):
#     if len(nums) <= 1:
#         return
#     start = 1
#     end = len(nums) - 1 
#     pivot = nums[0]

#     while start <= end:
#         print(start, end)
#         if nums[start] > pivot and nums[end] < pivot:
#             tmp = nums[start]
#             nums[start] = nums[end]
#             nums[end] = tmp


#         if nums[end] < pivot and start < len(nums) - 1:
#             start += 1

#         elif nums[start] > pivot and end > 0:
#             end -= 1
#         else:
#             start += 1
#             end -= 1

#     tmp = nums[end]
#     pivot = nums[end]
#     nums[end] = tmp

#     quicksort(nums[0:end])
#     quicksort(nums[start:len(nums)])

# quicksort(nums)
# print(nums)