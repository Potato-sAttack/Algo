# 문자열 numbers의 각 자리를 연결하여 만들 수 있는 소수의 개수 return

from itertools import permutations # 순열
                
def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    lst = set()
    
    for i in range(1,len(numbers)+1):
        # 길이가 i인 순열 생성
        for j in permutations(numbers, i):
            # permutations는 튜플 형태로 반환되므로 각 자리를 합쳐준 다음 int형으로 변환
            a = int(''.join(j))
            lst.add(a)
                
    for i in lst:
        cnt = 0
        if i == 0 or i == 1: continue
        for x in range(2, i):
            if i % x == 0:  # 소수가 아니면
                cnt = 1
                break
        if cnt == 0:    # 소수이면
            answer += 1
            
    return answer

numbers = "011"
print(solution(numbers))