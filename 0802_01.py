def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        sliced_array = array[i - 1:j]  # i번째부터 j번째까지 자르기
        sorted_array = sorted(sliced_array) # 정렬
        answer.append(sorted_array[k - 1])  # k번째 숫자 추가
    return answer
