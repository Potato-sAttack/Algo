# 1번 수포자: 1,2,3,4,5 반복
# 2번 수포자: 2,1, 2,3, 2,4, 2,5 반복
# 3번 수포자: 3,3, 1,1, 2,2, 4,4, 5,5 반복

def solution(answers):
    result = []
    best = []
    
    person = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for p in person:
        score = 0
        j = 0
        for i in answers:   # 채점
            if i == p[j]: score += 1
            j += 1
            if j >= len(p): j = 0
        
        result.append(score)
        
    big = max(result)
    
    for i in range(len(result)):    # 최고점수 찾기
        if result[i] == big:
            best.append(i+1)
            
    return sorted(best)

answers = [1,3,2,4,2]
print(solution(answers))