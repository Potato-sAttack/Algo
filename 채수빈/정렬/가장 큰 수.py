# numbers 배열의 숫자를 이어붙여 나온 수 중에서 가장 큰 수 반환
# 문자열로 return

from functools import cmp_to_key

# while문 사용하면 시간초과 발생하여 따로 함수 작성
def compare(x,y):
    if x+y >= y+x:
        return -1
    else:
        return 1

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compare))
    # i = 0
    # while i != len(numbers)-1:
    #     a = numbers[i]
    #     b = numbers[i+1]
    #     if a + b < b + a:
    #         numbers[i], numbers[i+1] = b, a
    #         i = 0
    #     else: i += 1
    
    # '000'이 아닌 '0'을 반환하기 위해 int로 변환 후 str로 변환    
    answer = str(int(''.join(numbers)))
    
    return answer

numbers =  [454, 45]
print(solution(numbers))