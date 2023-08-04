"""
프로그래머스 - 완전탐색 > 모의고사

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

"""

def solution(answers):
    answer = []
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0] 
    
    # 완전탐색 - 반복문 구현
    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            scores[0] += 1
        if answers[i] == student2[i % len(student2)]:
            scores[1] += 1
        if answers[i] == student3[i % len(student3)]:
            scores[2] += 1
            
    max_score = max(scores)
    for i, score in enumerate(scores): # enumerate: 반복을 돌면서 인덱스와 요소를 튜플로 반환
        if score == max_score:
            answer.append(i + 1)  # max_score와 일치하는 score에 해당하는 학생 번호 i+1을 answer 리스트에 append
    
    return answer
