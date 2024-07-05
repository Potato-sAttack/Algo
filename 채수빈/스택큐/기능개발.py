# 진도가 100% 일 때 배포 and 앞에 있는 기능부터 순서대로 배포 and 하루에 한번 배포
# progresses = 배포 순서대로 작업의 진도가 적힌 정수 배열
# speeds = 작업의 개발 속도가 적힌 정수 배열
# return 각 배포마다 배포되는 기능의 개수

import math

def solution(progresses, speeds):
    answer = []
    day = []
    
    # 걸리는 기간 계산해서 day 배열 생성
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))
    
    cur = day.pop(0)
    cnt = 1
    while day:
        if day and cur >= day[0]:   # 오늘 배포할 작업보다 뒤에 작업이 day가 작으면 같이 배포
            cnt += 1
            day.pop(0)
        else:
            answer.append(cnt)
            cur = day.pop(0)    # answer에 추가해주고 cur와 cnt 재설정
            cnt = 1

    answer.append(cnt)
    
    return answer

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# print(solution(progresses, speeds))