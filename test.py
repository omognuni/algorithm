from collections import deque
res = [['apple'],['orange'],['cat, dog, elephant']]

res[2] = list(deque(['dog','cat', 'elephant']))

print(res)