N = int(input())

d = [0] * int(1e6 + 1)

# 틀린 풀이
# for i in range(2, N + 1):
#     d[i] = i
    
#     if i % 3 == 0:
#         d[i] = d[i//3] + 1


#     if i % 2 == 0: 
#         d[i] = d[i//2] + 1

#     d[i] = min(d[i-1] + 1, d[i])

for i in range(2, N + 1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
print(d[N])


N = int(input())

d = [0] * int(1e6 + 1)


print(d[N])