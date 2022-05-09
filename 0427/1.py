k = int(input())

d = [0]*(k+1)

for i in range(1, k+1):
    d[i] = i
    if i % 5 == 0:
        d[i] = int(i/5)
        continue
        
    if i % 3 == 0 and i % 5 != 0:
        d[i] = int(i/3)

    j = 1
    while (i-3*j)>=0:
        if (i - 3*j) % 5 == 0 and (i-3*j) != 0:
            d[i] = min(d[3*j] + d[(i-3*j)], d[i])
        j += 1
    if d[i] == i:
        d[i] = -1
        

print(d[k])
