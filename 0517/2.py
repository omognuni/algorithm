'''
https://www.acmicpc.net/problem/10250
'''
import sys
input = sys.stdin.readline

k = int(input())
ans = []
for i in range(k):
    h, w, n = map(int, input().split())
    r = n // h + 1
    f = n %  h
    # 배수인 경우 생각 안했음
    if not f:
        r = n // h
        f = h
    

    ans.append("{:d}{:02d}".format(f,r))

for _,value in enumerate(ans):
    print(value)