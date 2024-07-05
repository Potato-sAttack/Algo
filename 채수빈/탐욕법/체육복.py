# n = 전체 학생 수
# lost = 도난당한 학생 번호 배열
# reserve = 여벌 체육복을 가져온 학생 번호 배열
# return 수업 들을 수 있는 학생 최댓값

def solution(n, lost, reserve):
    # 여벌 체육복을 가져왔으며 도난당한 학생 제거 (중복 제거)
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    
    for i in reserve_only:
        if i-1 in lost_only:
            lost_only.remove(i-1)
        elif i+1 in lost_only:
            lost_only.remove(i+1)
            
    return n - len(lost_only)

# n = 5
# lost = [4,5]
# reserve = [3,4]
# print(solution(n, lost, reserve))