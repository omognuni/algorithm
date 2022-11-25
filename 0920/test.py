import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1

    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()  # 왼쪽 방향으로 회전
    nx = x + dx[direction]  # 현재 방향으로 이동
    ny = y + dy[direction]  # 현재 방향으로 이동

    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 이동을 했는데, 방문하지 않았거나, 빈 공간인 경우
        d[nx][ny] = 1  # 이동한 위치에서 청소, 0->1
        x = nx  # 위치 이동
        y = ny  # 위치 이동
        count += 1  # 청소를 했음으로 1 증가
        turn_time = 0  # 왼쪽 방향 회전 횟수 0으로 초기화
        continue  # 반복

    else:  # 이동이 불가능 한 경우 왼쪽 방향 회전, 횟수 증가
        turn_time += 1

    if turn_time == 4:  # 총 4번 회전 한 경우, 네 방향 모두 청소가 되어 있거나 벽이 있는 경우
        nx = x-dx[direction]  # 바라보는 방향에서 뒤로 이동
        ny = y-dy[direction]  # 바라보는 방향에서 뒤로 이동

        if array[nx][ny] == 0:
            x = nx  # 이동
            y = ny  # 이동

        else:  # 그렇지 않으면,
            break  # 작동을 멈춤
        turn_time = 0  # 왼쪽 방향 회전 횟수 초기화

print(count)  # count 값 출력
