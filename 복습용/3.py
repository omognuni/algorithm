def solution(n, m):
    res = []
    
    def dfs():
        
        if len(res) == m:
            print(" ".join(map(str, res)))
            return
        
        for i in range(1, n+1):
            if i not in res:
                res.append(i)
                dfs()
                res.pop()
    
    dfs()
    
    return

solution(3, 1)