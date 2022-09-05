import sys
input = sys.stdin.readline

n, m = map(int,input().split())

pokemon = {}
for i in range(1, n+1):
    p = input().strip('\n')
    pokemon[i] = p
    pokemon[p] = i
answer = []
for i in range(m):
    answer.append(input().strip('\n'))

for i in range(len(answer)):
    try:
        print(pokemon[int(answer[i])])
    except:
        print(pokemon[answer[i]])
