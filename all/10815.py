import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card = sorted(card)

m = int(input())
nums = list(map(int, input().split()))

def binary_search(arr, t, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            end = mid - 1
        else:
            start = mid + 1

    return None

result = []
for i in range(len(nums)):
    res = binary_search(card, nums[i], 0, n-1)
    if res != None:
        result.append(1)
    else:
        result.append(0)        
[print(i, end=' ') for i in result]