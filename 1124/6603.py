import sys
input = sys.stdin.readline

def dfs(start):
    if len(res) == 6:
        print(" ".join(map(str,res)))
        return
    
    for i in range(start, len(S)):
        if S[i] not in res:
            res.append(S[i])
            dfs(i+1)
            res.pop()            
    return


while True:
    kS = list(map(int, input().split()))

    k = kS[0]
    if k == 0:
        break
    S = kS[1:]

    res = []

    dfs(0)
    print()
