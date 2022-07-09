import sys
input = sys.stdin.readline

S = list(input().strip('\n'))

p = set()

for i in range(len(S)):
    for j in range(len(S)-i):
        p.add("".join(S[j:j+i+1]))

print(len(p))