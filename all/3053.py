import sys
import math
input = sys.stdin.readline

n = int(input())

euclid = (n**2)*math.pi
taxi = (n*2**(1/2))**2

print(euclid)
print(taxi)
