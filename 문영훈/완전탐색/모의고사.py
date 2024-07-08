def solution(answers):
    answer = []
    temp =[0,0,0]
    l1=[1,2,3,4,5]
    l2=[2,1,2,3,2,4,2,5]
    l3=[3,3,1,1,2,2,4,4,5,5]
    while answers:
        i=answers.pop(0)
        p= l1.pop(0)
        q= l2.pop(0)
        r= l3.pop(0)
        if i == p:
            temp[0]+=1
        if i == q:
            temp[1]+=1
        if i == r:
            temp[2]+=1
        l1.append(p)
        l2.append(q)
        l3.append(r)
    if temp[0] == max(temp):
        answer.append(1)
    if temp[1]== max(temp):
        answer.append(2)
    if temp[2]== max(temp):
        answer.append(3)
    
    return answer

"""
무지성 for문 + if문 + 큐를 리스트로..
"""