# s = 문자열

# 여는괄호는 push
# 닫는괄호면 arr에 들어있는 여는괄호 pop. 만약 arr이 비었으면 False

def solution(s):
    answer = True
    
    str = list(s)   # 문자열을 리스트로 변환
    arr = []
    
    for i in str:
        if i == '(':
            arr.append(i)
        elif i == ')':
            if arr == []:
                return False
            else:
                arr.pop()

    if arr != []: return False
    return True

# s = "()()"
# print(solution(s))