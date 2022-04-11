'''
https://programmers.co.kr/learn/courses/30/lessons/43162
'''


def solution(n, computers):

    nets = []
    visited = [False] * n

    start = 0
    while False in visited:
        net = []
        dfs(start, computers, visited, net)
        #print(visited, net)
        nets.append(net)
        start += 1
    tmp = []
    for net in nets:
        if net:
            tmp.append(net)
    nets = tmp
    answer = len(nets)
    return answer


def dfs(start, computers, visited, net):

    if visited[start]:
        return

    visited[start] = True
    net.append(start)
    for i in range(len(computers[start])):
        if computers[start][i] == 1:
            dfs(i, computers, visited, net)
