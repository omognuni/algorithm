import sys
input = sys.stdin.readline

answer = []
while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break
    
    if y % x == 0:
        answer.append('factor')
    
    elif x % y == 0:
        answer.append('multiple')

    else:
        answer.append('neither')

[print(ans) for ans in answer]