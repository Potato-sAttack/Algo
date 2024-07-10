def solution(brown, yellow):
    answer = []
    area = brown + yellow 
    
    for i in range(2, area):
        if area % i == 0:
            w = area // i   # 가로
            h = i   # 세로
            if (w-1) + (h-1) == brown // 2 and (w-2) * (h-2) == yellow:
                answer.append(w)
                answer.append(h)
                break
    
    return answer

# brown = 10
# yellow = 2
# print(solution(brown, yellow))