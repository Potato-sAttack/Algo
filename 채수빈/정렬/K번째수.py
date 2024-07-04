# commands = [i, j, k]


def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        arr = sorted(array[i-1:j])  # i번째부터 j번째까지 자르고 정렬 후 저장
        answer.append(arr[k-1]) # k번째 값 추출
    
    # for i in range(len(commands)):
    #     arr = []    # 자른 배열 담기
    #     for j in range(commands[i][0], commands[i][1]+1):
    #         arr.append(array[j-1])
    #     arr.sort()
    #     answer.append(arr[commands[i][2]-1])
    
    return answer

# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))