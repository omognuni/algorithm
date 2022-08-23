import sys
input = sys.stdin.readline

n = int(input())
count = 0
s = []
res = []
no = True

for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        s.append(count)
        res.append("+")

    if s[-1] == x:
        s.pop()
        res.append("-")

    else:
        no = False

if no == False:
    print("NO")

else:
    print("\n".join(res))
