"""
프로그래머스 - 최댓값과 최솟값
"""

def solution(s):
    num = [int(x) for x in s.split()] # 공백 기준으로 분리 - int 변환 - list에 저장
    answer = str(min(num)) + ' ' + str(max(num)) # str으로 변환하여 하나로 합침
    return answer
