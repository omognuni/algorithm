import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sets = {}
for i in range(n):
    sets[input().strip('\n')] = 1

words = []
for i in range(m):
    words.append(input().strip('\n'))

count = 0

for i in range(len(words)):
    try:
        if sets[words[i]]:
            count+=1
    except:
        continue

print(count)