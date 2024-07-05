""" 완주하지 못한 선수 문제(7/4)"""
def solution(participant, completion):
    p_dic={}
    answer=""
    
    for i in participant:
        if i in p_dic :
            p_dic[i]+=1
        else:
            p_dic[i]=1
    
    for i in completion:
        p_dic[i]-=1
    
    for i in p_dic:
        if p_dic[i] !=0:
            return i
"""
설명
participant 의 사람명을 키로하고 사람수를 value로하는 dic만들고
completion의 명단에 있으면 사람수를 빼준다
0이 아니면 completion에 없었단 소리 -> return
""" 