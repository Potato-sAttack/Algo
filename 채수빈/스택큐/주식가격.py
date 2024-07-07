# prices = 초 단위로 기록된 주식 가격 배열
# return 가격이 떨어지지 않은 기간

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    cnt = 0
    
    while prices:
        i = prices.popleft()
        cnt = 0
                
        for x in prices:
            cnt += 1
            if x < i:
                break
        answer.append(cnt)
    
    return answer

prices = [1,3,4,2,3]
print(solution(prices))