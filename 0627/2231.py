'''
https://www.acmicpc.net/problem/2231
'''
import sys
input = sys.stdin.readline

n = int(input())

answer = []

for i in range(n//2, n + 1):
    sum = 0
    tmp = i
    while tmp > 0:
        sum += tmp % 10
        tmp = tmp//10
    sum += i
    if sum == n:
        answer.append(i)
# 없는 경우 예외처리 안해서 IndexError
if answer:
    print(answer[0])
else:
    print(0)
