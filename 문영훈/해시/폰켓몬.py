"폰켓몬 문제(7/4)"

def solution(nums):
    max_choice_num=len(nums)/2
    a_dic={}
    for num in nums:
        if num in a_dic:
            a_dic[num]+=1
        else:
            a_dic[num]=1
    
    if len(a_dic)>=max_choice_num:
        answer=max_choice_num
    else:
        answer=len(a_dic)  
    
    return answer

"""
설명
1. 배열에 있는 폰켓몬들을 키로 하고, 폰켄몬 개수를 value로하는 a_dic 생성(해시)
2. 최대로 고를 수 있는 가짓수는 배열의 크기/2, 키가 존재한다->적어도 그 종류의 폰켄몬이 하나이상 존재 하므로
최대 가짓수로 뽑으려면 무조건 하나로 뽑아야 되니, 뽑아야 되는 최대 가짓수 = 키의 개수로 보고
키의 개수가 max_choice보다 클 때는 mac_choice보다 적게 뽑야야 되니 return을 max_choice로
그 외엔 키의 개수로...

"""