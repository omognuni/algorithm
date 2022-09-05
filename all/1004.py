import sys
import math
input = sys.stdin.readline


def in_planet(loc, planet):
    dist = math.sqrt((loc[0]-planet[0])**2 + (loc[1]-planet[1])**2)
    if dist <= planet[2]:
        return True
    return False


T = int(input())
ans = []

# 출발, 도착점이 다른 원 안에 있는 경우 무조건 통과, 같은 원인 경우 통과 x

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    planets = []
    count = 0

    k = int(input())

    for j in range(k):
        cx, cy, r = map(int, input().split())
        planets.append([cx, cy, r])

    for planet in planets:

        if in_planet([x1, y1], planet) and in_planet([x2, y2], planet):
            pass

        elif in_planet([x1, y1], planet):
            count += 1

        elif in_planet([x2, y2], planet):
            count += 1

    ans.append(count)

[print(i) for i in ans]
