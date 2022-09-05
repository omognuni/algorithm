import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

cards = {numbers[i]: 0 for i in range(n)}
for i in range(n):
    cards[numbers[i]] += 1

m = int(input())

numbers2 = list(map(int, input().split()))

for i in range(m):
    try:
        print(cards[numbers2[i]], end=' ')
    except:
        print(0, end=' ')
