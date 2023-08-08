"""
프로그래머스 - 가장 가까운 같은 글자
"""


def solution(s):
    answer = []
    loc_dic = {}
    
    for i, c in enumerate(s):
        if c in loc_dic:
            answer.append(i - loc_dic[c])
        else:  
            answer.append(-1)
        loc_dic[c] = i
    
    return answer
