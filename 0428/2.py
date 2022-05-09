# import heapq

# n, k = map(int, input().split())

# d = [[] for i in range(n+1)]
# l = []
# for i in range(n):
#     w, v = map(int, input().split())
#     l.append([w,v])

# d[0] = [0,0]
    
# for i in range(1, n+1):
#     heap = []
#     for _ in l:
#         heapq.heappush(heap, (_[1], _[0]))        
#     count = 0
#     total_value = 0
#     total_weight = 0
#     while count < i and heap:
#         value, weight = heapq.heappop(heap)
#         total_value += value
#         total_weight+= weight
        
#         if total_weight <= k:
#             d[i] = [total_weight, total_value]
#             d[i] = max(d[i-1], d[i], key=lambda x:x[1])
#             count += 1
            
#         else:
#             total_value -= value
#             total_weight -= weight
            
# answer = max(d, key=lambda x:x[1])
# print(answer[1])

n, k = map(int, input().split())

l = [[0,0]]

for i in range(n):
    w, v = map(int, input().split())
    l.append([w,v])
d = [[0] * (k+1) for i in range(n+1)] 


for i in range(1, n+1):
    for j in range(1, k+1):
        w = l[i][0]
        v = l[i][1]
        
        if j < w:
            d[i][j] = d[i-1][j]
        
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
            
print(d[n][k])