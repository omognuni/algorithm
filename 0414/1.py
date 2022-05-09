'''
https://programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq as hq

def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)
    h = []
    count = 0

    while scoville:
        # h 연산 끝나기 전에 끝나지 않도록 조건 추가 (not  h)
        if scoville[0] >= K and not h:
            return count
        h.append(hq.heappop(scoville))

        if len(h) == 2:
            count += 1
            total = h[0] + h[1] * 2

            h = []
            hq.heappush(scoville, total)


    return -1