
import sys
input = sys.stdin.readline

k = int(input())

k-= 1
i=0
while k>0:
    i += 1
    k -= 6*i

print(i+1)