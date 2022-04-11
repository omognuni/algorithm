'''
https://programmers.co.kr/learn/courses/30/lessons/42587
'''


from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque(priorities)

    index = [i for i in range(len(priorities))]

    iq = deque(index)

    new_q = []

    while q:

        v = q.popleft()
        t = iq.popleft()

        add = False

        for i in range(len(q)):
            if v < q[i]:
                q.append(v)
                iq.append(t)

                add = True

                break
        if add:
            continue
        else:
            new_q.append([v, t])

    for i in range(len(new_q)):
        if new_q[i][1] == location:
            answer = i + 1

    return answer


'''
짧은 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


'''
