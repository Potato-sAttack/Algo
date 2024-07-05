"""괄호검사(7/5)"""
def solution(s):
    answer = True
    list1=[]
    for i in s:
        if i == '(':
            list1.append(i)
        elif len(list1) !=0:
            list1.pop()
        else:
            answer=False
            break
    if len(list1) != 0:
        answer=False
    return answer



