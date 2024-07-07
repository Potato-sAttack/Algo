# 스코빌 지수가 가장 낮은 두 개의 음식을 섞어 새로운 음식을 만듦
# 섞은 음식의 스코빌 지수 = 가장 안 매운 음식의 스코빌 지수 + 두번째로 안 매운 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
# return 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1 return
# scoville = 배열

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) > 1 and scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1
        elif len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        else: break
    
    return answer

# scoville = [1, 2, 3, 9, 10, 12]
# K = 7
# print(solution(scoville, K))