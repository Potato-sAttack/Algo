def solution(nums):
    answer = 0
    dic = dict()
    
    for i in nums:
        if i in dic:    # dic에 이미 존재하는 번호이면 value값만 증가
            dic[i] += 1
        else:
            dic[i] = 1  # dic에 없으면 새로 추가
    
    for i in range(len(nums)//2):
        if i >= len(dic): break # i가 dic의 길이를 넘어가면 끝
        answer += 1
        
    return answer

# nums = [3,3,3,2,2,2]
# print(solution(nums))