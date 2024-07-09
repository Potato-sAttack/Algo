
def solution(bridge_length, weight, truck_weights):
    time=0
    bridge=[0]*bridge_length
    cur=0
    while len(truck_weights)!=0:
        time+=1
        cur-=bridge.pop(0)   
        
        if cur + truck_weights[0] <=weight:
            temp=truck_weights.pop(0)
            cur+=temp
            bridge.append(temp)
        else:
            bridge.append(0)
            
    time+=bridge_length

    return time

"""
트럭 - 1초에 한칸씩 이동
bridge length만큼 칸을 가지는 bridge를 큐로 만듬
매초마다+=1을 해주어 시간이 흐르고,birdge.pop을이용하여 칸이 움직이면서 제일 끝에 있는 칸의 요소를 비워줌
없을수도 있음 트럭이 있는 경우 현재 bridge의 무게에서 빼줘야 하므로 cur에 반환
 현재 들어갈 트럭의 무게랑 현재 다리위의 무게의 합이 한계 무게보다 작거나 같다면 트럭을 bridge위에 추가
 그게 아니라면 트럭이 추가안된 빈칸이 추가되는 것이므로 무게의 요소가 0인 bridge를 추가해주므로써 구현
"""