'''
https://www.acmicpc.net/problem/2869
'''
import sys
import math

input = sys.stdin.readline
a, b, v =map(int,input().split())

days = (v-a)/(a-b)
days = math.ceil(days)
print(int(days+1))