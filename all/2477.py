import sys
input = sys.stdin.readline

n = int(input())

tr = []
for i in range(6):
    d, l = map(int, input().split())
    tr.append([d, l])

tr += tr


sm = []
for i in range(len(tr)-3):
    if tr[i][0] == tr[i+2][0] and tr[i+1][0] == tr[i+3][0]:
        sm = tr[i:i+4]
        break


sm_sq = sm[1][1]*sm[2][1]
big_sq = (sm[0][1] + sm[2][1]) * (sm[1][1]+sm[3][1])
sq = big_sq - sm_sq
print(sq * n)
