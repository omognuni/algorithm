import sys
input = sys.stdin.readline

n = int(input())

numbers = []

numbers = list(map(int, input().split()))

numbers2 = set(numbers)
numbers2 = list(numbers2)

numbers2.sort()

for number in numbers:
    print(numbers2.index(number), end=' ')
