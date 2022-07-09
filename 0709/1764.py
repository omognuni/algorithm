import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nolisten = []
for i in range(n):
    name = input().strip('\n')
    nolisten.append(name)

nolisten = list(set(nolisten))
nosee = {}

# 0 인 경우 생각안함
for i in range(1,m+1):
    name = input().strip('\n')
    nosee[name] = i


answer = []
for i in range(len(nolisten)):
    try: 
        # 0 인 경우 생각안함
        if nosee[nolisten[i]]:
            answer.append(nolisten[i])
    except:
            pass

print(len(answer))
answer.sort()
[print(answer[i]) for i in range(len(answer))]

# nolisten = set()
# for i in range(n):
#     nolisten.add(input())

# nosee = set()
# for i in range(m):
#     nosee.add(input())

# answer = sorted(list(nolisten & nosee))
# print(len(answer))
# for i in answer:
#     print(i)