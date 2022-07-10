import sys
input = sys.stdin.readline

x,y,w,h = map(int, input().split())

x_dist = min(abs(w-x), abs(x-0))
y_dist = min(abs(h-y), abs(y-0))

print(min(x_dist,y_dist))