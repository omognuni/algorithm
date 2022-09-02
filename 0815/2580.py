import sys
input = sys.stdin.readline

board = []
zeros = []

for i in range(9):
    board.append(list(map(int, input().rstrip().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))


def check_row(x, n):
    for i in range(9):
        if board[x][i] == n:
            return False
    return True


def check_col(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True


def check_rect(x, y, n):
    rect_x = x // 3 * 3
    rect_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[rect_x + i][rect_y + j] == n:
                return False
    return True


def dfs(idx):

    if idx == len(zeros):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        x = zeros[idx][0]
        y = zeros[idx][1]

        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            board[x][y] = i
            dfs(idx+1)
            board[x][y] = 0


dfs(0)
