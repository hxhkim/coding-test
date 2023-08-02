"""
프로그래머스 두 개 뽑아서 더하기

정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):
    answer = list(set([numbers[i] + numbers[j] 
                       for i in range(len(numbers)) 
                       for j in range(i+1, len(numbers))]))
    answer.sort()
    return answer

# numbers에서 숫자 하나 선택 = i
# numbers에서 i를 제외한 다른 숫자 선택 = j
# set으로 중복 제거 -> list 변환 -> sort 정렬
