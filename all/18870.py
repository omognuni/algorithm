import sys
input = sys.stdin.readline

n = int(input())

numbers = []

numbers = list(map(int, input().split()))

numbers2 = list(sorted(set(numbers)))

dic = {numbers2[i]: i for i in range(len(numbers2))}

for i in numbers:
    print(dic[i], end=' ')