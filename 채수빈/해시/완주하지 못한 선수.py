# participant = 참여 선수 이름 배열
# completion = 완주 선수 이름 배열
# 완주하지 못한 선수 이름 return

def solution(participant, completion):
    answer = ''
    
    dic = dict()

    # 참여선수 dic 생성
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    # 완주선수 value 차감
    for i in completion:
        if i in dic:
            dic[i] -= 1
    
    # dic의 value가 0이면 완주
    for i in dic:
        if dic[i] != 0:
            answer += i
            
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["filipa", "marina", "nikola"]
print(solution(participant, completion))