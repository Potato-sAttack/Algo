# citations = 발표한 논문의 인용 횟수 배열
# H-Index = 논문 n편 중, h번 이상 인용된 논문이 h편 이상일 때 h의 최댓값
# 인용된 횟수가 h 이상?

def solution(citations):    
    h = 0
    citations.sort(reverse=True)
    print(citations)
    # h 보다 i가 크면 h를 증가시킴.
    for i in citations:
        if i > h:
            h += 1
    return h
        
    # 정렬 안쓰고 푼 답
    # h = len(citations)
    # cnt = 0
    # while True:
    #     for i in range(len(citations)):
    #         if citations[i] >= h:
    #             cnt += 1
    #     if cnt >= h: return h
    #     else: 
    #         h-= 1
    #         cnt = 0
    

citations = [3, 0, 6, 1, 5]
print(solution(citations))