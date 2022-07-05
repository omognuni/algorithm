import sys
input = sys.stdin.readline

n = int(input())

coords = []
for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

coords.sort(key=lambda x: (x[1], x[0]))
[print(''.join(str(coord).split(',')).strip('()')) for coord in coords]
