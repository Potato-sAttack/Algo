# clothes = 코니가 가진 의상들 2차원 배열 ([[이름, 종류]])
# return 서로 다른 옷 조합 수

# 안 입는 경우도 있으므로 종류별로 n,m개 있을 때 경우의 수는 (n+1)(m+1)-1 이다. 
# (-1을 하는 이유는 아무것도 입지 않는 경우는 제외해야 하기 때문)

def solution(clothes):
    answer = 1
    dic = dict()
    # 의상 딕셔너리 생성 (key: 종류, value: 개수)
    for name, type in clothes:
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
    
    for i in dic.values():
        answer *= i+1
                
    return answer-1

# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# print(solution(clothes))