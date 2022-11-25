import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
N = len(nums)

count = 0

subset = set()

def dfs(k,N,total):
    global count
    if k == n:
        if total == s:
            count +=1
        return
    
    dfs(k+1, N, total)
    dfs(k+1, N, total+nums[k])

    return
      
dfs(0, N, 0)
if s == 0:
    count -= 1
print(count)