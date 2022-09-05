'''
https://www.acmicpc.net/problem/1018
'''
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

chess = []

for i in range(n):
    l = list(input().strip('\n'))
    chess.append(l)


answer = []


for i in range(n-7):
    for j in range(m-7):
        count = [0, 0]
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] != 'B':
                        count[0] += 1
                    if chess[k][l] != 'W':
                        count[1] += 1

                else:
                    if chess[k][l] != 'W':
                        count[0] += 1
                    if chess[k][l] != 'B':
                        count[1] += 1
        answer.append(min(count[0], count[1]))

print(min(answer))


# 오답 코드

# tmp = copy.deepcopy(chess)
# start = ['B', 'W']
# answer = []


# for i in range(n-7):
#     for j in range(m-7):
#         count = [0, 0]
#         for s in range(2):
#             chess[0][0] = start[s]
#             if chess[0][0] != start[s]:
#                 count[s] += 1
#             for k in range(i, n-1):
#                 for l in range(j, m-1):
#                     if chess[k][l] == chess[k+1][l]:
#                         count[s] += 1
#                         if chess[k][l] == 'B':
#                             chess[k][l] = 'W'
#                         else:
#                             chess[k][l] = 'B'
#                     if chess[k][l] == chess[k][l+1]:
#                         count[s] += 1

#                         if chess[k][l] == 'B':
#                             chess[k][l] = 'W'
#                         else:
#                             chess[k][l] = 'B'

#             chess = copy.deepcopy(tmp)
#         answer.append(min(count[0], count[1]))

# print(answer)
