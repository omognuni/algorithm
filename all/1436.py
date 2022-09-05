'''
https://www.acmicpc.net/problem/1436
'''
import sys
input = sys.stdin.readline

n = int(input())

list_666 = []
list_666.append(666)
for i in range(2700000):
    if '666' in str(i):
        list_666.append(i)
    else:
        continue

print(list_666[n])
