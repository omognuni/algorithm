'''
'aaabbcccddabc''a*b*c*d*abc'
'''

def solution(sentence):
    answer = ''
    
    for i in range(len(sentence)):
        if sentence[i-1] == sentence[i]:
            if sentence[i+1] != sentence[i]:
                answer += '*'
                continue
            else:
                continue
        answer += sentence[i]
    return answer
        
sentence = 'aaabbcccddabc'
print(solution(sentence))