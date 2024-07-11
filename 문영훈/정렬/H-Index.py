def solution(citations):
    citations.sort(reverse=True)
    h= 0
    for p, q in enumerate(citations):
        if p + 1 <= q:
            h = p + 1
        else:
            break
    return h
"""
인용횟수 많은 순으로 정렬 후 for문을 돌면서 검사
p+1 = 현재 논문의 인용회수 이상을 만족하는 논문 개수 
q=현재 논문의 인용회수
만약 현재 논문의 인용회수보다 현재 논문 개수가 작거나 같다면 h에 1을 추가(아직까진 h가 h-idex 기준을 만족 x)
그다음 루프를 돌 때 만약 현재 논문의 인용회수보다 현재 논문 개수가 작다면 이 전 값이 기준을 만족하는 h이므로 break
"""