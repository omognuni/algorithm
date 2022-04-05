
class Solution:
    def search(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end + 1) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1

            if nums[mid] > target:
                end = mid - 1

        return -1


count = 0


def search(nums=[], target=0):
    global count
    if not nums:
        return -1

    mid = len(nums) // 2 - 1

    if mid < 0:
        mid = 0

    new_nums = []

    if nums[mid] == target:
        count += mid
        return count

    if nums[mid] < target:
        count += mid + 1
        new_nums = nums[mid+1:]
        return search(new_nums, target)

    if nums[mid] > target:
        count += mid - 1
        new_nums = nums[:mid-1]
        return search(new_nums, target)


ans = search([5], 5)

print(ans)
