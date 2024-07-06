# bridge_length = 다리에 올라갈 수 있는 최대 트럭 수
# weights = 다리가 견딜 수 있는 최대 무게
# truck_weights = 트럭 별 무게 배열
# return 모든 트럭이 다리를 건너는 데 걸리는 최소 시간

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * (bridge_length))
    cur_weight = 0
    
    while True:
        answer += 1
        cur_weight -= queue.popleft()

        # 다리 위 트럭 무게가 10 이하이고 개수가 2 이하일 때 다음 트럭을 다리로 올림
        if truck_weights and (cur_weight+truck_weights[0]) <= weight and len(queue) <= bridge_length:
            x = truck_weights.pop(0)
            queue.append(x)
            cur_weight += x
        # 다리 위에 더 이상 트럭을 올릴 수 없을 때
        else:
            queue.append(0)
        
        if cur_weight == 0: break
    
    return answer

bridge_length = 100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))