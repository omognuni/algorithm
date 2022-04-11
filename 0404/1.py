'''
프로그래머스 스택/큐 1번
https://programmers.co.kr/learn/courses/30/lessons/42586
'''


from collections import deque


def solution(progresses, speeds):

    answer = []

    q = deque(progresses)
    sq = deque(speeds)

    while q:
        v = 0
        done = []

        for i in range(len(q)):
            if q[i] >= 100:
                continue
            q[i] = q[i] + sq[i]

# IndexError: deque index out of range
# referencing index 0 of empty queue caused index error. 'q and' added to condition
        while q and q[0] >= 100:
            v = q.popleft()
            sq.popleft()
            done.append(v)

        if done:
            answer.append(len(done))

    return answer
