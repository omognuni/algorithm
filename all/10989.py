'''
https://www.acmicpc.net/problem/10989
'''
import sys
input = sys.stdin.readline

n = int(input())

nums = [0 for i in range(10001)]

for i in range(n):
    num = int(input())
    nums[num] += 1


for i in range(len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)


