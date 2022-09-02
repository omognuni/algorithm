import sys
input = sys.stdin.readline

n = int(input())

numbers1 = list(map(int, input().split()))
numbers1.sort()

m = int(input())

numbers2 = list(map(int, input().split()))


def binary_search(array, num):

    if len(array) == 0:
        return 0

    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == num:
            return 1

        elif array[mid] < num:
            start = mid + 1

        elif array[mid] > num:
            end = mid - 1

    return 0


for i in numbers2:
    print(binary_search(numbers1, i))
