"""
프로그래머스 - 모음 제거
"""

def solution(my_string):
    remove = ['a', 'e', 'i', 'o', 'u']
    
    for c in remove:
        my_string = my_string.replace(c, "")
        
    answer = my_string
    return answer
