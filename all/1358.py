import sys
import math
input = sys.stdin.readline


def is_inside(w, h, x, y, px, py):
    r = h//2
    dis1 = math.sqrt((px-x)**2 + (py-(y+r))**2)
    dis2 = math.sqrt((px-(x+w))**2 + (py-(y+r))**2)

    if px >= x and px <= x+w and py >= y and py <= y+h:
        return True
    elif dis1 <= r or dis2 <= r:
        return True
    else:
        return False


# W H X Y P, R=H/2
w, h, x, y, p = map(int, input().split())


count = 0
for i in range(p):
    px, py = map(int, input().split())
    if is_inside(w, h, x, y, px, py):
        count += 1
print(count)
