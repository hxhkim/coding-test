"""
프로그래머스 - 푸드파이트 대회
"""

def solution(food):
    half_food = [f // 2 for f in food] # 음식 갯수를 2로 나눈 몫을 리스트로 저장
    
    list_food = ''
    for i, f in enumerate(half_food):
        list_food += str(i) * f # 인덱스 번호를 갯수만큼 반복
    
	  answer = list_food + '0' + list_food[::-1]
        
    return answer
