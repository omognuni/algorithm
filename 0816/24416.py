import sys
input = sys.stdin.readline

n = int(input())


d = [0 for i in range(n+2)]

d[1] = 1
d[2] = 1

count1 = 0
count2 = 0


def rec_fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1

    else:
        return rec_fib(n-1) + rec_fib(n-2)


def fibo(n):
    global count2
    if n == 1 or n == 2:
        return d[n]

    for i in range(3, n + 1):
        count2 += 1
        d[i] = d[i-1] + d[i-2]

    return d[n]


rec_fib(n)
fibo(n)
print(count1, count2)
