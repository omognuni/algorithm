import sys
input = sys.stdin.readline

n = int(input())

p = []

for i in range(n):
    p.append(list(map(int, input().split())))

blue = 0
white = 0


def divide_square(papers, x1, x2, y1, y2):
    new_sq = []

    [new_sq.append(i[x1:x2]) for i in papers[y1:y2]]

    return new_sq


def recursive(papers):
    global white, blue

    if len(papers) == 0:
        return

    start = papers[0][0]

    x = len(papers)

    for i in range(x):
        for j in range(x):
            if start != papers[i][j]:
                sq1 = divide_square(papers, 0, x//2, 0, x//2)
                recursive(sq1)
                recursive(divide_square(papers, x//2, x, 0, x//2))
                recursive(divide_square(papers, 0, x//2, x//2, x))
                recursive(divide_square(papers, x//2, x, x//2, x))
                return

    if start == 0:
        white += 1

    elif start == 1:
        blue += 1


recursive(p)
print(white, blue)
