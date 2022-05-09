"""
 https://www.acmicpc.net/problem/1655

"""
import sys
import heapq

# 이거 때문에 시간 초과났다..
input = sys.stdin.readline

n = int(input())

l_h, r_h = [],[]

for i in range(n):
    k = int(input())
    if len(l_h) == len(r_h):
        heapq.heappush(l_h, (-k,k))
        
    else:
        heapq.heappush(r_h, k)
        
    if len(r_h) >= 1 and len(l_h) >= 1 and l_h[0][1] > r_h[0]:
        l = heapq.heappop(l_h)[1]
        r = heapq.heappop(r_h)
        
        heapq.heappush(l_h, (-r,r))
        heapq.heappush(r_h, l)
    
    print(l_h[0][1])
        
# import heapq as hq

# n = int(input())
# l_h = []
# r_h = []
# mid = int(input())
# for i in range(1, n):
#     k = int(input())
#     if k > mid:
#         hq.heappush(r_h, k)
#         if len(r_h) > len(l_h) + 1:
#             hq.heappush(l_h, (-mid, mid))
#             mid = hq.heappop(r_h)
#     else:
#         hq.heappush(l_h, (-k, k))
#         if len(l_h) > len(r_h):
#             hq.heappush(r_h, mid)
#             mid = hq.heappop(l_h)[1]
            
#     print(mid)
# ------------------------------------------------------------------
# def quick_sort(array):
    
#     if len(array)<1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]
    
#     left_side = [x for x in tail if x<=pivot]
#     right_side = [x for x in tail if x>pivot]
    
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# n = int(input())

# l=[]

# nums = []

# for i in range(n):
#     k = int(input())
#     l.append(k)
#     l = quick_sort(l)
#     nums.append(l[(len(l)-1)//2])
# for _, i in enumerate(nums):
#     print(i)


