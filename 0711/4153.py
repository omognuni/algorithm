import sys

input = sys.stdin.readline

tri = []
while True:
    sides = list(map(int, input().split()))
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        break
    sides.sort()
    tri.append(sides)


for t in tri:
    if t[0]**2 + t[1]**2 == t[2]**2:
        print('right')
    else:
        print('wrong')
