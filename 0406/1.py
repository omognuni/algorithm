'''
https://programmers.co.kr/learn/courses/30/lessons/43165
'''


def solution(numbers, target):
    answer = 0
    global count
    count = 0

    def bfs(i, op, total):
        global count

        if i >= len(numbers):
            if total == target:
                count += 1
            return

        total += numbers[i]*op
        bfs(i+1,  1, total)
        bfs(i+1, -1, total)

    op = [1, -1]

    for i in op:
        bfs(0, i, 0)

    answer = count/2
    return answer
