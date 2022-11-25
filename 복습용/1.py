import sys

def solution(k):
    answer = 0    
    num_list = [6,2,5,5,4,5,6,3,7,6]
              # 0 1 2 3 4 5 6 7 8 9
    d = [0 for _ in range(101)]
    
    for i in range(1, len(num_list)):
        d[num_list[i]] += 1
    
    # 바텀업
    # # for i in range(2, k):
    #     # d[i] = d[i] + 
    # for i in range(k+1):
    #     for j in range(len(num_list)):
    #         if i - num_list[j] >= 0:
    #             d[i] = d[i - num_list[j]] + d[i]
    #         # d[i + num_list[j]] = d[i] + d[i + num_list[j]]
    #             # d[8] = d[2], d[3], d[4].....
    # 탑다운
    
    # d[n] = d[n-k]
    print(d)
    return answer

print(solution(50))

# result = []


# def solution(k):
#     def dp(num):
#         if num in memo:
#             return memo[num]
#         elif num < 0:
#             return 0
#         memo[num] = 0
#         for key, v in stick_num.items():
#             memo[num] += dp(num - v)
#         return memo[num]

#     memo = {0:1}
#     stick_num = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
#     answer = 0
#     for key, v in stick_num.items():
#         if key != 0:
#             answer += dp(k - v)

#     if k == 6:
#         return answer + 1
#     else:
#         return answer

# print(solution(50))
'''
[6][9][1,5][5,1][1,1,1][7,7]
'''