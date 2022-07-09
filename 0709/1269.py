import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = []
A = set(map(int, input().split()))

B = []
B = set(map(int, input().split()))

inter = set(A & B)
print(len(A) + len(B) - 2*len(inter))