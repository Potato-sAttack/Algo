# priorities = 실행 대기 큐에 있는 프로세스의 중요도가 담긴 배열
# location = 몇 번째로 실행되는지 알고 싶은 프로세스의 위치
# return location의 프로세스가 몇 번째로 실행되는지

def solution(priorities, location):
    answer = 0
    
    # 실행대기 큐 생성
    queue = []
    for i in range(len(priorities)):
        queue.append(i)
    
    while location in queue:
        if len(priorities) == 1: 
            answer += 1
            break
        cur_location = queue.popleft()
        cur_prioritiy = priorities.pop(0)
        
        if cur_prioritiy >= max(priorities):
            answer += 1
        else:
            queue.append(cur_location)
            priorities.append(cur_prioritiy)
            
    return answer


    # 시간초과
    # while location in queue:
    #     stop = 0
    #     cur_location = queue.pop(0)
    #     cur_prioritiy = priorities.pop(0)
    #     
    #     for i in priorities:
    #         if cur_prioritiy < i:
    #             queue.append(cur_location)
    #             priorities.append(cur_prioritiy)
    #             stop = 1
    #             continue
    #     if stop == 1: continue
    #     else: answer += 1
    

# priorities = [2, 1, 3, 2]
# location = 2
# print(solution(priorities, location))