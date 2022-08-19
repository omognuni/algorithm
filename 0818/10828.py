import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = []
for i in range(n):
    line = input().split()
    cmd = line[0]
    if len(line) > 1:
        num = line[1]

    if cmd == 'push':
        stack.append(int(num))

    if cmd == 'top':
        if stack:
            ans.append((stack[-1]))
        else:
            ans.append(-1)

    if cmd == 'size':
        ans.append(len(stack))

    if cmd == 'empty':
        if len(stack) == 0:
            ans.append(1)
        else:
            ans.append(0)

    if cmd == 'pop':
        if stack:
            ans.append(stack.pop())

        else:
            ans.append(-1)

[print(i) for i in ans]
